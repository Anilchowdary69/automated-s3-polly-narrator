import boto3
import os
import urllib.parse

# Initialize clients
s3_client = boto3.client('s3')
polly_client = boto3.client('polly')

def lambda_handler(event, context):
    # 1. Get the bucket and file name from the S3 Trigger event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    
    # Define your destination bucket name here
    destination_bucket = "text-narrator-destinationbucket69"
    output_key = source_key.replace('.txt', '.mp3')

    try:
        # 2. Fetch the text file content from S3
        response = s3_client.get_object(Bucket=source_bucket, Key=source_key)
        text_content = response['Body'].read().decode('utf-8')

        # 3. Request speech synthesis from Polly
        polly_response = polly_client.synthesize_speech(
            Text=text_content,
            OutputFormat='mp3',
            VoiceId='Joanna',
            Engine='neural'
        )

        # 4. Upload the audio stream directly to the second S3 bucket
        if "AudioStream" in polly_response:
            s3_client.put_object(
                Bucket=destination_bucket,
                Key=output_key,
                Body=polly_response['AudioStream'].read(),
                ContentType='audio/mpeg'
            )
            
        print(f"Success! {source_key} converted to {output_key}")
        return {"status": "success"}

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
