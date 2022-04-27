import boto3

class DBController:

    def __init__(self) -> None:
        self.dynamoClient = boto3.client('dynamodb')
        self.loginTable = boto3.resource('dynamodb').Table("login")
        self.userTable = boto3.resource('dynamodb').Table("users")

    def GetAllLogins(self):
        return self.dynamoClient.scan(TableName='login')
    
    def Register(self, username, email, password):
        self.loginTable.put_item(
            TableName = 'login',
            Item = {
                "username": username,
                "email": email,
                "password": password 
            }
        )
    
    def GetUser(self, email):
        response = self.userTable.get_item(Key={"email": email})
        return response['Item']