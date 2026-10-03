# Lambda: MLRTT-translateAndSynthesize
# Version 1.2

import json
import boto3
import urllib.parse
import os
import time

s3 = boto3.client('s3')
translate = boto3.client('translate')
polly = boto3.client('polly')

# Custom LDS translation cache
dictionary_cache = {
	"sacrament": {
		"es": "sacramento",
		"ko": "성찬식"
	},
	"prophet": {
		"es": "profeta",
		"ko": "선지자"
	},
	"bishop": {
		"es": "obispo",
		"ko": "감독"
	},
	"Book of Mormon": {
		"es": "Libro de Mormón",
		"ko": "몰몬경"
	},
	"priesthood": {
		"es": "sacerdocio",
		"ko": "신권"
	}
	# Add more religious-specific terms as needed
}


def lambda_handler(event, context):
	bucket = event['Records'][0]['s3']['bucket']['name']
	key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
	job_id = key.split("/")[-1].replace(".json", "")

	# Load transcript
	transcript_obj = s3.get_object(Bucket=bucket, Key=key)
	transcript = json.loads(transcript_obj['Body'].read())
	segments = transcript['results'].get('items', [])

	english_segments = []
	for item in segments:
		if item.get('type') == 'pronunciation':
			english_segments.append(item['alternatives'][0]['content'])
		elif item.get('type') == 'punctuation':
			english_segments[-1] += item['alternatives'][0]['content']

	full_text = ' '.join(english_segments)

	# Save original voice using Polly
	generate_audio(full_text, 'original.mp3', bucket, voice_id='Joanna')

	# Translate and synthesize per language
	language_map = {
		"en": {"voice": "Joanna", "filename": "english.mp3"},
		"es": {"voice": "Lucia", "filename": "spanish.mp3"},
		"ko": {"voice": "Seoyeon", "filename": "korean.mp3"}
	}

	for lang_code, lang_info in language_map.items():
		translated = apply_cache_translation(full_text, lang_code)
		generate_audio(translated, lang_info['filename'], bucket, voice_id=lang_info['voice'])

	# Store JSON with translated texts for audit
	translation_metadata = {
		"original_text": full_text,
		"translations": {
			lang: apply_cache_translation(full_text, lang) for lang in language_map.keys()
		}
	}
	s3.put_object(
		Body=json.dumps(translation_metadata, ensure_ascii=False),
		Bucket=bucket,
		Key=f"output/{job_id}-translations.json"
	)

	return {
		"statusCode": 200,
		"body": "Audio files and translation metadata stored successfully."
	}


def apply_cache_translation(text, target_lang):
	translated = ''
	max_bytes = 9500  # safe buffer under 10,000

	# Build chunks under byte limit
	chunks = []
	current = ''
	for sentence in text.split('. '):
		if len((current + sentence).encode('utf-8')) > max_bytes:
			chunks.append(current.strip())
			current = sentence + '. '
		else:
			current += sentence + '. '
	if current:
		chunks.append(current.strip())

	# Translate chunk-by-chunk
	for chunk in chunks:
		response = translate.translate_text(
			Text=chunk,
			SourceLanguageCode='auto',
			TargetLanguageCode=target_lang
		)
		translated += response['TranslatedText'] + ' '

	return translated.strip()


def generate_audio(text, filename, bucket, voice_id='Joanna'):
	# Polly max is 3000 characters
	chunks = []
	current = ''
	for word in text.split():
		if len(current) + len(word) + 1 > 2900:
			chunks.append(current)
			current = word
		else:
			current += ' ' + word
	if current:
		chunks.append(current)

	# Generate & combine MP3s
	audio_paths = []
	for i, chunk in enumerate(chunks):
		resp = polly.synthesize_speech(Text=chunk.strip(), OutputFormat='mp3', VoiceId=voice_id)
		chunk_path = f'/tmp/{filename}_{i}.mp3'
		with open(chunk_path, 'wb') as f:
			f.write(resp['AudioStream'].read())
		audio_paths.append(chunk_path)

	# Combine using basic file append (for simplicity)
	final_path = f'/tmp/{filename}'
	with open(final_path, 'wb') as final_file:
		for path in audio_paths:
			with open(path, 'rb') as chunk:
				final_file.write(chunk.read())
			os.remove(path)

	s3.upload_file(final_path, bucket, f'output/{filename}')
	os.remove(final_path)
