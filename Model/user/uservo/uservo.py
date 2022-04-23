# userdb table
# email(str), pwd(str), name(str)

class UserVO:
    def __init__(self,email,pwd,name):
        self.email = email;
        self.pwd = pwd;
        self.name = name;

    def getEmail(self):
        return self.email;
    def getPwd(self):
        return self.pwd;
    def getName(self):
        return self.name;

    def setEmail(self,email):
        self.email = email;
    def setPwd(self,pwd):
        self.pwd = pwd;
    def setName(self,name):
        self.name = name;

    def __str__(self):
        return '{} {} {}'.format(self.email,self.pwd,self.name)
    def print(self):
        return f'{self.email}',f'{self.pwd}',f'{self.name}'
