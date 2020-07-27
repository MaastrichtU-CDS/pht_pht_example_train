import os 
import pandas as pd
import json

#This part consists reading database url from env variable and setting the data query

# read database uri
database_uri = os.getenv('DATABASE_URI','no_database_uri')

# read/query data from database_uri
data = pd.read_csv(database_uri)


## paste your algorithm here . Example to calculate mean age from the data
count = len(data)
mean = data['Age'].mean()

#json code your output
result = {
    'Number of Rows': count,
    'Average age':mean
}

# Write output to file
with open('output.txt', 'w') as f:
    f.write(json.dumps(result))

