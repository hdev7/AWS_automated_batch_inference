import boto3
import paramiko
#import sys
def worker_handler(event, context):

    s3_client = boto3.client('s3')
    #Download private key file from secure S3 bucket
    s3_client.download_file('my-ml-auto','my-ml-auto/keys/ec2.pem', '/tmp/ec2.pem')

    k = paramiko.RSAKey.from_private_key_file("/tmp/ec2.pem")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host=event['IP']
    print("Connecting to " + host)
    c.connect( hostname = host, username = "ec2-user", pkey = k )
    print("Connected to " + host)

    commands = [
        "aws s3 cp s3://my-ml-auto/scripts/scoring_script.py --region us-east-1 /home/ec2-user/scoring_script.py",
        "aws s3 cp s3://my-ml-auto/scripts/model.pkl --region us-east-1 /home/ec2-user/model.pkl",
        "aws s3 cp s3://my-ml-auto/scripts/tfidfvectorizer.pkl --region us-east-1 /home/ec2-user/tfidfvectorizer.pkl",
        "aws s3 cp a3://my-ml-auto/inputs/test.csv --region us-east-1 /home/ec2-user/test.csv",
        "source ml_project/bin/activate",
        "python /home/ec2-user/scoring_script.py /home/ec2-user/test.csv",
        "deactivate",
        "aws s3 cp /home/ec2-user/scored_data.csv s3://my-ml-auto/outputs/scored_data.csv"
        ]

    for command in commands:
        print("Executing {}".format(command))
        stdin , stdout, stderr = c.exec_command(command)
        print(stdout.read())
        print(stderr.read())

    return
    {
        'message' : "Script execution completed. See Cloudwatch logs for complete output"
    }
