import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! ENJOY !!!!!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
