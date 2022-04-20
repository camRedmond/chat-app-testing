from crypt import methods
from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, firestore, auth
import json

cred = credentials.Certificate("./chat-15049-firebase-adminsdk-k4mme-768cee88ac.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


app = Flask(__name__)
app.debug = True


# Main chat room page
@app.route("/messages", methods=["GET"])
def getAllMessages():
    # get all messages stored in firestore cloud database
    # messages are returned as json object and passed throught this function to react

    # TO-DO
    # limit messages to max 50 at a time
    messages = []
    docs = db.collection('messages').stream()
    for doc in docs:
        messages.append(doc.to_dict())

    # return json.dumps(messages, indent=4, sort_keys=True, default=str)
    return messages[0]

@app.route("/users", methods=["GET"])
def getAllUsers():
    # get all users stored in firestore cloud database

    users = []
    docs = db.collection('users').stream()
    for doc in docs:
        users.append(doc.to_dict())

    return json.dumps(users, indent=4, sort_keys=True, default=str)

@app.route("/newuser/<username>", methods=["POST"])
def createNewUser():
    # Check if username or password is not null or too long
    # Check if username already exists
    username = request.json.get('username')
    # password = request.json.get('password')

    print('NEW USER ADDED:',{username})

    # hash password before entering database

    # return new user







@app.route("/login", methods=["POST"])
def login():
    return



if __name__ == '__main__':
    app.run(host='0.0.0.0')