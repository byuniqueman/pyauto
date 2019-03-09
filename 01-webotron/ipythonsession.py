import boto3
session = boto3.Session(profile_name='pyauto')
s3 = session.resource('s3')
