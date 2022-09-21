import json
from datetime import datetime
import boto3
import os
import uuid

dbtable_name = str(os.environ['DYNAMODB_TABLE'])
dynamodb = boto3.resource('dynamodb', region_name=str(os.environ['REGION_NAME']))

def get_user(event, context):
    print("Displaying user info")
    
    table = dynamodb.Table(dbtable_name)
    item_response = table.get_item(Key={
        'parent_id': event['pathParameters']['parent_id']
    })
    
    item = item_response['Item']
    response = {
        "statusCode": 200,
        "headers":{
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(item),
            'isBase64Encoded': False
        }
    return response

def create_user(event, context):
    print("Adding a user")
    table = dynamodb.Table(dbtable_name)
    table_response = table.put_item(
        Item=json.loads(event["body"])
    )

    response = {
        "statusCode": 200, 
        "body": json.dumps(table_response), 
        "headers": {'Content-Type': 'application/json'}
    }
    
    return response
