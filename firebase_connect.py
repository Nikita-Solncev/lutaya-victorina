import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def connect_to_database():
    """
    подключаемся к Firebase Realtime Database
    """

    cred = credentials.Certificate('firebase database key.json')

    firebase_admin.initialize_app(cred, {
        'databaseURL': "YOUR URL"
    })

    return db.reference('users data')
