import os
import boto3
from dotenv import load_dotenv

load_dotenv('.env')

class Database:
    def __init__(self):
        if os.environ.get('PRODUCTION') == '0':
            self.dynamodb = boto3.resource(
                'dynamodb',
                endpoint_url="http://localhost:8000")
            self.dynamodb_client = boto3.client(
                'dynamodb',
                endpoint_url="http://localhost:8000")
        else:
            self.dynamodb = boto3.resource(
                'dynamodb',
                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                region_name="us-east-1"
                )
            self.dynamodb_client = boto3.client(
                'dynamodb',
                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                region_name="us-east-1"
                )


    def put_item(self, table_name, document):
        table = self.dynamodb.Table(table_name)
        response = table.put_item(Item=document)
        return response


    def update_item(self, table_name, artist, songs):
        table = self.dynamodb.Table(table_name)

        response = table.update_item(
            Key={
                'name': artist
            },
            UpdateExpression="set songs=:s",
            ExpressionAttributeValues={
                ":s": songs
            }
        )
        return response


    def check_existence(self, table_name, query):
        table = self.dynamodb.Table(table_name)
        response = table.get_item(Key=query)
        return False if response is None else True


    def delete_item(self, table_name, query):
        table = self.dynamodb.Table(table_name)
        table.delete_item(Key=query)


    def get_table(self, table_name):
        table = self.dynamodb.Table(table_name)
        return table


    def create_table(self):
        existing_tables = self.dynamodb_client.list_tables()['TableNames']
        if 'artists' not in existing_tables:
            table = self.dynamodb.create_table(
                TableName='artists',
                KeySchema=[
                    {
                        'AttributeName': 'name',
                        'KeyType': 'HASH'
                    },
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'name',
                        'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )