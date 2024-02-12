from app import app, mongo

@app.route('/')
def home():
    # Test MongoDB connection
    mongo.db.myCollection.insert_one({"message": "Hello, MongoDB!"})
    return "Connected to MongoDB and inserted a document."
