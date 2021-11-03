import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('kop147-firstproject-firebase-adminsdk-yncym-8ea714c323.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kop147-firstproject-default-rtdb.asia-southeast1.firebasedatabase.app/'})

'''ref = db.reference('new/newer/newest').child('mai').update({'mai':'mak mak'})'''

ref = db.reference('')
delete_mai = ref.child('new/newer/older/oldest/new')
delete_mai.delete()

# CRUD create read update delete
