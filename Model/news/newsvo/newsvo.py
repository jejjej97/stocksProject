# userdb table
# email(str), pwd(str), name(str)

class NewsVO:
    def __init__(self,title,link,press,dtime):
        self.title = title;
        self.link = link[:-27];
        self.press = press
        self.dtime = dtime

    def getTitle(self):
        return self.title;
    def getLink(self):
        return self.link;
    def getPress(self):
        return self.press;
    def getDtime(self):
        return self.dtime;

    def setTitle(self,title):
        self.title = title;
    def setLink(self,link):
        self.link = link;
    def setPress(self, press):
        self.press = press;
    def setDtime(self, dtime):
        self.dtime = dtime;

    def __str__(self):
        return '{} {} {} {}'.format(self.title, self.link, self.press, self.dtime)
