import json 
import boto3
dynamoDB = boto3.resource('dynamodb')
table = dynamoDB.Table('santizerAppDB')
def lambda_handler(event, context):
    name=event['Name']
    print("name:")
    print(name)
    resp= table.get_item(Key={"Name":name})
    print(resp)
    return resp['Item']