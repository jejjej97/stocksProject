# userdb table
from Model.bookmark.bookmarksql.bookmarksql import bookmarkSql
from Model.bookmark.bookmarkvo.bookmarkvo import bookmarkVO
from Model.sqlitedao import SqliteDao

class bookmarkDAO(SqliteDao):

    def __init__(self,dbNAme):
        super().__init__(dbNAme);

    def insert(self, u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(bookmarkSql.insert_bookmarkdb, (u.getemail(),u.getstockname(),u.geturl()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('Insert Completed: %s' % u);

    def delete(self,u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(bookmarkSql.delete_bookmarkdb, ('%'+u.getemail()+'%',u.getstockname(), u.geturl()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('삭제 되었습니다.');

    def alldelete(self):
        try:
            conn = self.getConn();
            conn['cursor'].execute(bookmarkSql.alldelete_bookmarkdb);
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('전부 삭제 되었습니다.');

    def select(self, u):
        users = [];
        conn = self.getConn();
        conn['cursor'].execute(bookmarkSql.select_bookmarkdb, ('%'+u.getemail()+'%',u.getstockname(), u.geturl()))
        all = conn['cursor'].fetchall();
        for u in all:
            rs = bookmarkVO(u[0], u[1], u[2]);
            users.append(rs);
        self.close(conn);
        return users;

    def selectall(self, email):
        users = [];
        conn = self.getConn();
        conn['cursor'].execute(bookmarkSql.selectall_bookmarkdb, ('%'+email+'%',))
        all = conn['cursor'].fetchall();
        for u in all:
            rs = bookmarkVO(u[0], u[1], u[2]);
            users.append(rs);
        self.close(conn);
        return users;

    def stockname(self, email):
        users = [];
        conn = self.getConn();
        conn['cursor'].execute(bookmarkSql.stockname_bookmarkdb, ('%'+email+'%',))
        all = conn['cursor'].fetchall();
        for u in all:
            rs = bookmarkVO(u[0], u[1], u[2]);
            users.append(rs);
        self.close(conn);
        return users;


if __name__ == '__main__':
    print('start test');

    sqlitedao = SqliteDao('shop');
    sqlitedao.makeTable();
    bookmarkdao = bookmarkDAO('shop');


    # Insert Test
    # b1 = bookmarkVO('아무');
    # b1.setemail('dd')
    # b1.seturl('asdf')

    # b1=bookmarkVO('jejej97@naver.com','현대','http://naver.com')
    # try:
    #     bookmarkdao.insert(b1);
    #     print('OK');
    # except Exception as e:
    #     print('error',e);


    # Delete Test
    # try:
    #     bookmarkdao.delete();
    #     print('OK');
    # except Exception as e:
    #     print('에러 내용',e);

    # b = bookmarkVO('jejej97@naver.com', '현대', 'http://naver.com')
    # print(b)
    # # Select All
    # result = bookmarkdao.select(b);
    # for u in result:
    #    print(u);

    # stockname
    result = bookmarkdao.stockname('jejej97@naver');
    for u in result:
        print(u);

    print('end test');