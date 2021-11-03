import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('kop147-firstproject-firebase-adminsdk-yncym-8ea714c323.json')
# kop mark: get this file by generate key in firebase website:
# under project overview setting > project setting > service account then generate the key file

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kop147-firstproject-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
# copy from head of database on firebase.com

# As an admin, the app has access to read and write all data, regardless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())