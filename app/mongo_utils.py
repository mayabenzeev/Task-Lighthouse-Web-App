from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
client = None
db = None


def get_mongo_client():
    """create a single MongoClient and db instance and reuse it throughout the application."""
    global client, db
    if client is None:
        uri = (f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_CLUSTER_URL')}"
               f"/?retryWrites=true&w=majority&appName=dev")
        # Create a new client and connect to the server
        client = MongoClient(uri)
        db = client.task_lighthouse_db
    return db


def add_user(user_data):
    """Adds a user if they do not already exist."""
    try:
        db = get_mongo_client()
        if not db.users.find_one({"user_id": user_data['user_id']}):
            db.users.insert_one(user_data)
            return "User added successfully."
        else:
            return "User already exists."
    except Exception as e:  # avoid crashes
        return f"An error occurred: {str(e)}"


def add_project(project_data):
    """Inserts a new project into the database."""
    try:
        db = get_mongo_client()
        db.projects.insert_one(project_data)
        return "Project added successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_user_projects(user_id):
    """Fetches projects associated with a user."""
    try:
        db = get_mongo_client()
        projects = db.projects.find({"members": user_id})
        return list(projects)
    except Exception as e:
        return f"An error occurred: {str(e)}"

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
