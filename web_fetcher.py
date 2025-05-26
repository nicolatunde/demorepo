
import requests as req
from pprint import pprint


users = req.get('https://jsonplaceholder.typicode.com/users').json()
print (users)

def fetch_user_data():

    users_list= []
    
    for user in users:
        users_list.append(user['name'])
    
    return users_list

