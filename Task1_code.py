import boto3
import json
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('inventory')

def insert_item(event, context):
    request_body = json.loads(event['body'])
    item_name = request_body['name']
    item_category = request_body['category']
    item_price = request_body['price']
    timestamp = str(datetime.datetime.utcnow())

    # Check if item already exists
    response = table.get_item(
        Key={
            'name': item_name
        }
    )

    if 'Item' in response:
        # Update existing item
        item = response['Item']
        item['price'] = item_price
        item['last_updated_dt'] = timestamp
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({'id': item['id']})
        }
    else:
        # Insert new item
        item_id = table.scan()['Count'] + 1
        item = {
            'id': item_id,
            'name': item_name,
            'category': item_category,
            'price': item_price,
            'last_updated_dt': timestamp
        }
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({'id': item_id})
        }
