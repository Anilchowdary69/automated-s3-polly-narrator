
An event-driven, serverless pipeline that automatically converts text files into high-quality MP3 audio using Amazon Polly, AWS Lambda, and Amazon S3.

Key Features
Zero-Touch Automation: Uses S3 Event Notifications to trigger processing the moment a file is uploaded.

Multi-Bucket Support: Designed to handle uploads from multiple source buckets into a single centralized audio repository.

Production-Grade Security: Implements a Customer Managed Policy following the Principle of Least Privilege.

Neural TTS Engine: Utilizes Amazon Polly’s Neural engine for natural, human-like speech synthesis.

🏗️ Architecture Workflow:
https://uploads.teachablecdn.com/attachments/XjgRDlKQiCwI639iKnPA_4A.png

process:
Trigger: S3 sends a s3:ObjectCreated event notification to the Lambda function.

Process: * Lambda fetches the text content from the source bucket.

Lambda sends the text to Amazon Polly for synthesis.

Store: Lambda streams the resulting MP3 back to the Destination S3 Bucket.

Setup & Installation:
1. IAM Configuration
Create a Lambda Execution Role and attach the Least Privilege policy. This ensures the Lambda can only access specific resources
2. Lambda Setup
create a lamda function using python by using my above python code.

3. S3 Event Trigger
Navigate to your Source Bucket in the AWS Console.

Go to Properties > Event Notifications.

Create an event for All object create events.

Destination: Your Lambda function.

or you can add triggers at the lamda as well

use case:
Simply upload any .txt file to your source bucket. Within seconds, a corresponding .mp3 file will appear in your destination bucket named audio-[timestamp].mp3.
