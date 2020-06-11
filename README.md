# AWS_automated_batch_inference
Automated the batch inference using AWS Coud Infrastructure ( Severless | Event driven arcitecture )

- Created a text classification model, which can label whether a tweet is about a disaster or not. 
- Automated the batch inferencing of unlabelled tweets in AWS using Amazon S3 events, Amazon Lambda (Serverless), Amazon EC2

Overview:
- If a dataset to be scored is dropped in the S3 bucket, it will automatically trigger a lambda function which spins up an EC2 instances and scores the data. 
- The scored data is loaded back into the output bucket and the EC2 instances will be stopped as soon as this happens. 
- This effort reduced around 90% costs on AWS Services
- This architecture is event driven and serverless. Hence, no supervision requried.

Architecture Demo:

![Architecture Demo](https://github.com/hdev7/hdev7.github.io/blob/master/images/aws_project_demo.png)
