import json
import boto3

dynamoDB=boto3.resource('dynamodb')
table=dynamoDB.Table('santizerAppDB')


def lambda_handler(event, context):
    print(event)
    table.put_item(Item=event)
    return{
        "code": 200,
        "message" : "Data is successfully inserted",
    }
