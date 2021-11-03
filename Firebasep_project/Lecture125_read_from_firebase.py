import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('kop147-firstproject-firebase-adminsdk-yncym-8ea714c323.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kop147-firstproject-default-rtdb.asia-southeast1.firebasedatabase.app/'})

ref = db.reference('users')
print(ref.get())

print((db.reference('text_demo')).get())

user2_age = db.reference('/users/chaivit/age')
print(user2_age.get())

user2_email = db.reference('/users/chaivit/email')
print(user2_email.get())

user2 = db.reference('/users/chaivit')
print(user2.get())
