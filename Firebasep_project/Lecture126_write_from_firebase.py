import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('kop147-firstproject-firebase-adminsdk-yncym-8ea714c323.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kop147-firstproject-default-rtdb.asia-southeast1.firebasedatabase.app/'})

ref = db.reference('')
user_ref = ref.child('users')

#ex1
'''user_ref.update({
    'drcom': {'age': '59', # can not use special character for keys
                'tel': '0811234567',
                'email': '1234@gmail.com'},
    'mrb': {'age': '40',
                'tel': '0899888888',
                'email': '888@gmail.com'}
})'''



# set = input new data by replacing new data to old data to that path
# update = insert new data
# push = insert new data with new unique directory
# transaction - ?

