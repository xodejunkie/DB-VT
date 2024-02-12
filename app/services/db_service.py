from app import mongo, db
from app.models.sql_models import User
from app.models.nosql_models import UserDocument

def create_user(username):
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

def get_user(user_id):
    return User.query.get(user_id)

def insert_document(collection, document):
    user_doc = UserDocument.create_user_doc(document['username'])
    mongo.db[collection].insert_one(user_doc)
