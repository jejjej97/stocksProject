# userdb table
# email(str), pwd(str), name(str)

class bookmarkVO:
    def __init__(self,email,stockname,url):
        self.email = email;
        self.stockname = stockname;
        self.url = url;

    def getemail(self):
        return self.email;
    def getstockname(self):
        return self.stockname;
    def geturl(self):
        return self.url;

    def setemail(self,email):
        self.email = email;
    def setstockname(self,stockname):
        self.stockname = stockname;
    def seturl(self,url):
        self.url = url;

    def __str__(self):
        # return f'{self.email}', f'{self.stockname}', f'{self.url}'
        return '{} {} {}'.format(self.email, self.stockname, self.url)
    def pr(self):
        return f'{self.email}', f'{self.stockname}', f'{self.url}'
