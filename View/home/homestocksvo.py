# userdb table
# email(str), pwd(str), name(str)

class homestocksvo:
    def __init__(self,num,url,name,price,udprice,rate,sign):
        self.num = num;
        self.url = url;
        self.name = name;
        self.price = price;
        self.udprice = udprice;
        self.rate = rate;
        self.sign = sign;

    def getnum(self):
        return self.num;
    def geturl(self):
        return self.url;
    def getname(self):
        return self.name;
    def getprice(self):
        return self.price;
    def getudprice(self):
        return self.udprice;
    def getrate(self):
        return self.rate;
    def getsign(self):
        return self.sign;

    def setnum(self, num):
        self.num = num;
    def seturl(self, url):
        self.url = url;
    def setname(self, name):
        self.name = name;
    def setprice(self, price):
        self.price = price;
    def setudprice(self, udprice):
        self.udprice = udprice;
    def setrate(self, rate):
        self.rate = rate;
    def setsign(self, sign):
        self.rate = sign;


    def print(self):
        return f'{self.num}',f'{self.url}',f'{self.name}',f'{self.price}',f'{self.udprice}',f'{self.rate}',f'{self.sign}'
