

import json
from typing import List
from urllib import response
from Models.user import User
from Models.login import Login

class ModelController:
    
    def __init__(self, DBController) -> None:
        self.db = DBController
        self.Logins = list()
        self.users = list()
        
    def RegisterUser(self, username, email, password):
        self.Logins.append(Login(username, email, password))
        
    def GetLogins(self):
        response = self.db.GetAllLogins()
        for login in response['Items']:
            self.Logins.append(Login(login['username']['S'], login['email']['S'], login['password']['S']))
            print(login['username']['S'])
    
    def GetUser(self, email):
        response = self.db.GetUser(email)
        user = User(response['email'], response['username'], response['subs'])
        return user