# userdb table
from Model.sqlitedao import SqliteDao
from Model.user.usersql.usersql import userSql
from Model.user.uservo.uservo import UserVO
# from home.errorcode import ErrorCode 에러코드

class UserDAO(SqliteDao):

    def __init__(self,dbNAme):
        super().__init__(dbNAme);

    def insert(self, u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(userSql.insert_userdb, (u.getEmail(),u.getPwd(),u.getName()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('Insert Completed: %s' % u);

    def delete(self, u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(userSql.delete_userdb, (u.getEmail(),u.getPwd(),u.getName()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('%s 삭제 되었습니다.' % id);

    def update(self, u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(userSql.update_userdb,(u.getPwd(), u.getName(), u.getEmail()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);
        print('%s 수정 되었습니다.' % u.getEmail());

    def select(self, email):
        uservo = None;
        conn = self.getConn();
        conn['cursor'].execute(userSql.select_userdb,(email,));
        rs = conn['cursor'].fetchone();
        uservo = UserVO(rs[0], rs[1], rs[2]);
        self.close(conn);
        return uservo;

    def selectall(self):
        users = [];
        conn = self.getConn();
        conn['cursor'].execute(userSql.selectall_userdb);
        all = conn['cursor'].fetchall();
        for u in all:
            rs = UserVO(u[0],u[1],u[2]);
            users.append(rs);
        self.close(conn);
        return users;



if __name__ == '__main__':
    print('start test');

    sqlitedao = SqliteDao('shop');
    sqlitedao.makeTable();
    userdao = UserDAO('shop');

    # Insert Test
    user1 = UserVO('as1243@naver.com','pwd15','정말숙');
    try:
        userdao.insert(user1);
        print('OK');
    except:
        print('ErrorCode.E0001');
    # Delete Test
    # user1 = UserVO('asdf2@naver.com', 'pwd15', '정말숙');
    # try:
    #     userdao.delete(user1);
    #     print('OK');
    # except:
    #     print(ErrorCode.E0001);
    # Update Test
    # user2 = UserVO('as2@naver.com', 'pwd54', 'kim1');
    # userdao.update(user2);
    #
    # Select
    # user3 = userdao.select('as1231232@naver.com');
    # print(user3);

    # Select All
    result = userdao.selectall();
    for u in result:
       print(u);


    print('end test');