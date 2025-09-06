from pymongo import MongoClient,errors

def connecting_to_mongodb():
    try:
        # client = MongoClient("mongodb://host.docker.internal:27017/", serverSelectionTimeoutMS=10000)
        client = MongoClient("mongodb://localhost:27017/myDB", serverSelectionTimeoutMS=10000)
        return client
    except errors.ServerSelectionTimeoutError as e:
        # Timeout specific error
        raise RuntimeError(f"MongoDB connection timed out: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"MongoDB connection error: {str(e)}")
