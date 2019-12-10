import os 
import pandas as pd
import json

database_uri = os.getenv('DATABASE_URI','no_database_uri')

test = pd.read_csv(database_uri)
mean = test['Age'].mean()

result = {'Average age':mean}

# Write output to file
with open('output.txt', 'w') as f:
    f.write(json.dumps(result))





#host = os.getenv('HOST','no host')
#api_path = os.getenv('API_PATH','no api path')
#port = os.getenv('PORT','no port')
#data = pd.read_csv(database_uri)
#print(data)

# results = {
#         'database': data,
#
#     }


#print(results)

# with open('output.txt', 'w') as f:
#     f.write(json.dumps(results))