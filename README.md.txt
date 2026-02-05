🎙️ Automated AWS Polly Narrator (Least-Privilege Edition)
An event-driven, serverless pipeline that automatically converts text files into high-quality MP3 audio using Amazon Polly, AWS Lambda, and Amazon S3.

🌟 Key Features
Zero-Touch Automation: Uses S3 Event Notifications to trigger processing the moment a file is uploaded.

Multi-Bucket Support: Designed to handle uploads from multiple source buckets into a single centralized audio repository.

Production-Grade Security: Implements a Customer Managed Policy following the Principle of Least Privilege (no FullAccess wildcards).

Neural TTS Engine: Utilizes Amazon Polly’s Neural engine for natural, human-like speech synthesis.

🏗️ Architecture Workflow
Upload: A .txt file is uploaded to a designated "Source" S3 Bucket.

Trigger: S3 sends a s3:ObjectCreated event notification to the Lambda function.

Process: * Lambda fetches the text content from the source bucket.

Lambda sends the text to Amazon Polly for synthesis.

Store: Lambda streams the resulting MP3 back to the Destination S3 Bucket.

🛠️ Setup & Installation
1. IAM Configuration
Create a Lambda Execution Role and attach the following Least Privilege policy. This ensures the Lambda can only access specific resources:

JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3SourceAccess",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::YOUR_SOURCE_BUCKET/*.txt"
        },
        {
            "Sid": "S3DestAccess",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::YOUR_DESTINATION_BUCKET/*.mp3"
        },
        {
            "Sid": "PollyAccess",
            "Effect": "Allow",
            "Action": "polly:SynthesizeSpeech",
            "Resource": "*"
        }
    ]
}
2. Lambda Setup
Runtime: Python 3.12+

Handler: lambda_function.lambda_handler

Environment Variables: Ensure you update the destination_bucket variable in the code to match your bucket name.

3. S3 Event Trigger
Navigate to your Source Bucket in the AWS Console.

Go to Properties > Event Notifications.

Create an event for All object create events.

Suffix: .txt (Crucial to prevent loops).

Destination: Your Lambda function.

📝 Usage
Simply upload any .txt file to your source bucket. Within seconds, a corresponding .mp3 file will appear in your destination bucket named audio-[timestamp].mp3.