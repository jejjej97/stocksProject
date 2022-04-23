import sqlite3

from Model.bookmark.bookmarksql.bookmarksql import bookmarkSql
from Model.news.newssql.newssql import NewsSql
from Model.user.usersql.usersql import userSql

class SqliteDao:
    def __init__(self, dbName):
        self.__dbName = dbName;
    def getConn(self):
        con = sqlite3.connect(self.__dbName);
        cursor = con.cursor();
        return {'con':con,'cursor':cursor};
    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close();
        if cc['con'] != None:
            cc['con'].close();
    def makeTable(self):
        cc = self.getConn();
        cc['cursor'].execute(userSql.make_userdb);
        cc['cursor'].execute(NewsSql.make_newsdb);
        cc['cursor'].execute(bookmarkSql.make_bookmarkdb);
        cc['con'].commit();
        self.close(cc);