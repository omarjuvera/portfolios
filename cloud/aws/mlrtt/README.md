# MLRTT — Multilingual Congregation Translation

Omar Juvera · Santa Monica College · CS 79F (1737), Machine Learning on AWS · June 2025

An AWS prototype that converts uploaded service video into translated audio for English-, Spanish- and Korean-speaking congregations. I built the project independently for my final project, with a practical community use in mind.

## What was completed

The submitted workflow used S3 uploads, Lambda with an FFmpeg layer, Amazon Transcribe language identification, Amazon Translate and Amazon Polly. The provided archive contains a completed 4,101-word English transcription, translations for `en`, `es` and `ko`, four MP3 outputs and AWS screenshots. The final report identifies CS 79F and describes an automated pipeline after manual video upload.

The church liked the project, but ongoing AWS charges prevented adoption. It chose Zoom's native translation. This release makes the recovered source available for study and reuse; a Zoom API integration is a future project.

## Scope

This is an uploaded-video batch prototype. The original final-project title described a real-time goal; continuous live audio streaming, Zoom API integration, voice-gender matching and latency benchmarking were not completed in the final submission. No church deployment or ongoing service use is claimed.

## Recovered source

- `source/transcribe_audio.py`: archived working transcription handler; responds to an S3 WAV upload and starts a Transcribe job with automatic language identification and a `transcribe/` output prefix.
- `source/translate_and_synthesize_v1_2.py`: archived version 1.2; loads transcription JSON, splits translation and speech requests, generates language outputs and saves metadata.
- `source/lds_terms_fragment.txt`: recovered, incomplete domain-vocabulary dictionary fragment, preserved as text rather than runnable code. Its presence does not establish that every dictionary entry was applied in the running pipeline.
- `evidence.json`: a manifest of inspected artifacts with hashes and sizes; no sermon text, audio or AWS account information.

The extraction stage is documented in the final report and screenshots, but a standalone extraction Python file was not found in the ZIP. No extraction implementation has been invented for this release.

## Reuse and deployment checklist

This source is preserved as historical project code, not a turnkey deployment package. `boto3` is required (included in the AWS Python Lambda runtime); install it locally if inspecting outside Lambda. The extraction function additionally requires an FFmpeg Lambda layer. Keep S3 and functions in the intended region and configure service permissions and prefix-filtered S3 events for audio and transcription outputs. AWS usage is billable; set a budget before running cloud jobs.

Before deploying, address the original prototype's limits: second-resolution job names can collide; fixed output filenames overwrite prior jobs; very long single sentences may exceed translation byte limits; punctuation assumes a preceding word; same-language output handling and MP3 concatenation need review. The file named `original.mp3` is synthesized from the transcript in the recovered version, not proof that the unchanged source recording was preserved. Validate source language, voices, job isolation, retries and event-loop prevention against current AWS documentation. Reconstruct and test the missing extraction stage.

## Verification for this release

Both published Python files pass syntax parsing. The manifest was generated from the uploaded ZIP, and its transcription status is `COMPLETED`. No new cloud deployment or AWS end-to-end execution was performed for this publication. Final-project operation is documented by the supplied report/artifacts and my confirmation.

## Next work

1. Organize and document the recovered project publicly.
2. Reconstruct the AWS deployment configuration and extraction stage from the original notes.
3. Improve cost controls, error handling and per-job outputs.
4. Explore Zoom API integration for the congregation's chosen platform.

The existing repository license applies. FFmpeg binaries and source congregation media are not redistributed in this release.
