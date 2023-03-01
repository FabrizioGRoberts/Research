import pandas as pd
import numpy as np

import datetime
import time
import json
import pyrebase


#Initialize app

def driver(file):
    data = pd.read_csv(file)
    [r,c] = data.shape

    for i in range(r):
        yield (float(data.loc[i].iat[0]),float(data.loc[i].iat[21]))
    
config = {
  "apiKey": "AIzaSyCDg23IRODfllEAcmXlsxo-0kX3OVXtAgs",
  "authDomain": "co2data1.firebaseapp.com",
  "databaseURL": "https://co2data1-default-rtdb.firebaseio.com",
  "storageBucket": "co2data1.appspot.com",
  "serviceAccount": "co2data1-firebase-adminsdk-2ylle-df5b0fb661.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

db.remove()
 
it=0
for i in driver('test.csv'):
    #key is ms from start
    if it==0:
        start = i[0]
        it+=1
    db.child("data").child(int(1000*(i[0]-start))).set(i[1])
    
