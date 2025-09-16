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
    #Now this lambda function find a person with name and password and tell his/her hobies
    for record in event['Records']:
        try:
            userName = json.loads(record['body'])['userName']
            password = json.loads(record['body'])['password']
            hobbies  = json.loads(record['body'])['hobbies']

            user = {
                "userName": userName ,
                "password":password ,
                "hobbies":hobbies
            }
            result = collection.find_one(user)
            if result:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "message": f"User {userName} already exists."
                    })
                }

            result = collection.insert_one(user)
            if result:
                return {
                    "statusCode": 200,
                    "_id": str(result.inserted_id),
                    "body": json.dumps({
                        "message": f"User {userName} added successfully."
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
#         "Records": [{
#             "body": json.dumps({
#                 "userName": "JohnDoe junior",
#                 "password": "securepassword",
#                 "hobbies": ['reading', 'gaming']
#             })
#         }]
#     }
#     context = {}
#     response = lambda_handler(event, context)
#     print(response)
