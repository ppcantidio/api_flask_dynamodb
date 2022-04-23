from flask_dynamo import Dynamo


dynamo = Dynamo()


def init_app(app):
    app.config['DYNAMO_TABLES'] = [
        {
            "TableName": "artists",
            "KeySchema": [
                { 
                    "AttributeName": "name",
                    "KeyType": "HASH"
                }
            ],
            "AttributeDefinitions": [
                {
                    "AttributeName": "name",
                    "AttributeType": "S"
                },
            ],
            "ProvisionedThroughput": {
                "ReadCapacityUnits": 10,
                "WriteCapacityUnits": 10
            }
        }
    ]
    dynamo.init_app(app)
    dynamo.create_all()
