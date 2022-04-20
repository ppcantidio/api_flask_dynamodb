import os
import boto3
from dotenv import load_dotenv

load_dotenv('.env')

class Database:
    def __init__(self):
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name="us-east-1"
            )

    def put_item(self, table_name, document):
        table = self.dynamodb.Table(table_name)
        response = table.put_item(Item=document)

        return response

    def get_item(self, table_name, query):
        table = self.dynamodb.Table(table_name)
        response = table.get_item(Key=query)
        item = response['Item']

        return item

    def delete_item(self, table_name, query):
        table = self.dynamodb.Table(table_name)
        table.delete_item(Key=query)

    def get_table(self, table_name):
        table = self.dynamodb.Table(table_name)
        return table