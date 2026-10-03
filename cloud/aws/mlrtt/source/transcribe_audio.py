# Works_lattests
import boto3
import time
import urllib.parse
import botocore.exceptions

transcribe = boto3.client('transcribe')
s3 = boto3.client('s3')

def lambda_handler(event, context):
	try:
		bucket = event['Records'][0]['s3']['bucket']['name']
		key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
		job_name = f"mlrtt-{int(time.time())}"

		file_uri = f"s3://{bucket}/{key}"
		output_key = f"transcribe/{job_name}.json"

		# Launch Transcribe job
		transcribe.start_transcription_job(
			TranscriptionJobName=job_name,
			Media={'MediaFileUri': file_uri},
			MediaFormat='wav',
			IdentifyLanguage=True,
			OutputBucketName=bucket,
			OutputKey=output_key
		)

		return {
			'statusCode': 200,
			'body': f"Started Transcribe job: {job_name}, output will be at: {output_key}"
		}

	except botocore.exceptions.ClientError as e:
		print(f"ClientError: {e}")
		return {
			'statusCode': 500,
			'body': f"Transcribe failed: {str(e)}"
		}
