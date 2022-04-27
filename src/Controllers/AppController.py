from Controllers.DBController import DBController
from Controllers.ModelController import ModelController
from Controllers.DatabaseSeed import SeedDatabase

class AppController:
    def __init__(self) -> None:
        self.db = DBController()
        self.modelController = ModelController(self.db)
        self.modelController.GetLogins()
        SeedDatabase.SeedDatabase("music")
    
    
    def Login(self, _email, password):
        validLogin = False
        
        for login in self.modelController.Logins:
            if login.email == _email:
                if login.password == password:
                    validLogin = True
                    
        return validLogin
    
    def GetUser(self, email):
        return self.modelController.GetUser(email)
    
    def Register(self, _email, password, _username) -> str:
        error = "None"
        for login in self.modelController.Logins:
            if login.email == _email:
                error = "Email already registered."
            elif login.username == _username:
                error = "Username already registered"
        
        if error == "None":
            self.modelController.RegisterUser(_username, _email, password)
            self.db.Register(_username, _email, password)
        
        return error