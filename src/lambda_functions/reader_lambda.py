import json
from src.utils.mongodb_connection import connecting_to_mongodb


def lambda_handler(event, context):
    try:
        client = connecting_to_mongodb()
        db = client["myDB"]
        collection = db["hobbies"]
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
    for record in event['Records']:
        try:
            userName = json.loads(record['body'])['userName']
            password = json.loads(record['body'])['password']

            user = collection.find_one({
        "$and": [
            {"userName": userName},
            {"password": password}
            ]
            })
            if user:
                hobbies = user.get("hobbies", [])
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "message": f"Hello {userName}, your hobbies are: {hobbies} "
                    })
                }
            else:
                return {
                    "statusCode": 404,
                    "body": json.dumps({
                        "message": "User not found or incorrect password."
                    })
                }
        except Exception as e:
            return {
                "statusCode": 500,
                "body": str(e)
            }

# if __name__ == "__main__":
#     # Example event for local testing
#     event = {
#         "body": json.dumps({
#             "userName": "JohnDoe junior",
#             "password": "securepassword"
#         })
#     }
#     context = {}
#     response = lambda_handler(event, context)
#     print(response)

