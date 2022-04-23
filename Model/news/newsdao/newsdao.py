# userdb table
from Model.news.newssql.newssql import NewsSql
from Model.news.newsvo.newsvo import NewsVO
from Model.sqlitedao import SqliteDao

# from home.errorcode import ErrorCode 에러코드

class NewsDAO(SqliteDao):

    def __init__(self,dbNAme):
        super().__init__(dbNAme);

    def insert(self, u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(NewsSql.insert_newsdb, (u.getTitle(),u.getLink(),u.getPress(),u.getDtime()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);

    def delete(self):
        try:
            conn = self.getConn();
            conn['cursor'].execute(NewsSql.delete_newsdb)
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('전체 삭제 완료');

    def select(self, title):
        news = [];
        conn = self.getConn();
        conn['cursor'].execute(NewsSql.select_newsdb, ('%'+title+'%',));
        all = conn['cursor'].fetchall();
        for u in all:
            rs = NewsVO(u[0],u[1],u[2],u[3]);
            news.append(rs);
        self.close(conn);
        return news;

    def selectall(self):
        news = [];
        conn = self.getConn();
        conn['cursor'].execute(NewsSql.selectall_newsdb);
        all = conn['cursor'].fetchall();
        for u in all:
            rs = NewsVO(u[0],u[1],u[2],u[3]);
            news.append(rs);
        self.close(conn);
        return news;


if __name__ == '__main__':
    print('start test');

    sqlitedao = SqliteDao('shop');
    sqlitedao.makeTable();
    newsdao = NewsDAO('shop');


    # Delete Test
    # try:
    #     newsdao.delete();
    #     print('OK');
    # except:
    #     print('ErrorCode.E0001');

    # Insert Test
    # news1 = NewsVO('뭐임','이거');
    #
    # newsdao.insert(news1);
    # print('OK');

    # Select
    news2 = newsdao.select('오');
    print(news2);
    for u in news2:
        print(u);

    # Select All
    # result = newsdao.selectall();
    # print(result)
    # for u in result:
    #    print(u);


    print('end test');