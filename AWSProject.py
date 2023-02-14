import requests
import json
import boto3
from urllib import request
from bs4 import BeautifulSoup
import json
from twilio.rest import Client

# Replace YOUR_API_KEY with your actual API key
api_key = ""

# Specify the endpoint for the API call
endpoint = "https://api.football-data.org/v4/competitions/SA/scorers"
endpoint2 = "http://api.football-data.org/v4/competitions/PL/standings"

# Add the API key to the headers
headers = {"X-Auth-Token": api_key}

# Make the GET request
response = requests.get(endpoint, headers=headers)
responsedata=response.json()

response2 = requests.get(endpoint2, headers=headers)
responsedata2=response2.json()

# Print the status code of the response
with open('data.json', 'w') as json_file:
    json.dump(responsedata["scorers"] , json_file)
   
    

# Print the data returned by the API
with open('C:\\Users\\User\\data.json','r') as datafile:
  records=json.load(datafile)


access_key=""
secret_access_key=""
session=boto3.Session(aws_access_key_id=access_key,aws_secret_access_key=secret_access_key, region_name='eu-central-1')
s3 = session.client('s3')

bucket_name = 'proiectiot'
file_name = "data.json"
  
# Use the S3 client to upload the file
s3.upload_file(datafile.name, bucket_name, file_name,
 ExtraArgs={'ACL': 'public-read'})


message_text=  # Insert your message here
print(message_text) 
account_sid = ''  # Insert your twillo account_sid
auth_token = ''  # Insert your twillo auth_token
client = Client(account_sid, auth_token)
from_phone_number = ''
to_phone_number = ''


message = client.messages.create(   
  body=message_text,
  from_=from_phone_number,
  to=to_phone_number
    )