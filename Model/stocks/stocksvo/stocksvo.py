# stocksvo.py

class StockVO:
    def __init__(self,rank,name,srate,nprice,yrate,updownrate,tamount,mprice,high,low,per,roe,sign,link):
        self.rank = rank;
        self.name = name;
        self.srate = srate;
        self.nprice = nprice;
        self.yrate = yrate;
        self.updownrate = updownrate;
        self.tamount = tamount;
        self.mprice = mprice;
        self.high = high;
        self.low = low;
        self.per = per;
        self.roe = roe;
        self.sign = sign;
        self.link =link;

    def getRank(self):
        return self.rank;
    def getName(self):
        return self.name;
    def getSrate(self):
        return self.srate;
    def getNprice(self):
        return self.nprice;
    def getYrate(self):
        return self.yrate;
    def getUpdownrate(self):
        return self.updownrate;
    def getTamount(self):
        return self.tamount;
    def getMprice(self):
        return self.mprice;
    def getHigh(self):
        return self.high;
    def getLow(self):
        return self.low;
    def getPer(self):
        return self.per;
    def getRoe(self):
        return self.roe;
    def getSign(self):
        return self.sign;
    def getLink(self):
        return self.link;

    def setRank(self,rank):
        self.rank =rank;
    def setName(self,name):
        self.name =name;
    def setSrate(self,srate):
        self.srate =srate;
    def setNprice(self,nprice):
        self.nprice =nprice;
    def setYrate(self,yrate):
        self.yrate =yrate;
    def setUpdownrate(self,updownrate):
        self.updownrate =updownrate;
    def setTamount(self,tamount):
        self.tamount =tamount;
    def setMprice(self,mprice):
        self.mprice =mprice;
    def setHigh(self,high):
        self.high =high;
    def setLow(self,low):
        self.low =low;
    def setPer(self,per):
        self.per =per;
    def setRoe(self,roe):
        self.roe =roe;
    def setSign(self,sign):
        self.sign =sign;
    def setLink(self,link):
        self.link =link;

    def print(self):
        return f'{self.rank}',f'{self.name}',f'{self.srate}',f'{self.nprice}',f'{self.yrate}',f'{self.updownrate}',f'{self.tamount}',f'{self.mprice}',f'{self.high}',f'{self.low}',f'{self.per}',f'{self.link}',f'{self.sign}',f'{self.num}',