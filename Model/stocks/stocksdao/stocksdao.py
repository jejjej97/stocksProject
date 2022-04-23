# stocksdao.py

from Model.sqlitedao import SqliteDao
from Model.stocks.stockssql.stockssql import StocksSql
from Model.stocks.stocksvo.stocksvo import StockVO


class StocksDAO(SqliteDao):

    def __init__(self, dbName):
        super().__init__(dbName);

    def insert(self, u):
        try:
            conn = self.getConn();
            conn['cursor'].execute(StocksSql.insert_stocksdb,(u.getRank(), u.getStock(), u.getSrate(), u.getNprice(), u.getYrate(), u.getUpdownrate(), u.getTamount(), u.getMprice(), u.getHigh(), u.getLow(), u.getPer(), u.getRoe(), u.getLink()));
            conn['con'].commit();
        except:
            raise Exception;
        finally:
            self.close(conn);

    def delete(self):
        try:
            conn = self.getConn();
            conn['cursor'].execute(StocksSql.delete_stocksdb)
            conn['con'].commit()
        except:
            raise Exception;
        finally:
            self.close(conn);

    def selecatall(self):
        stocks = []
        conn = self.getConn();
        conn['cursor'].execute(StocksSql.selectall_stocksdb);
        all = conn['cursor'].fetchall();
        for u in all:
            rs = StockVO(u[0],u[1],u[2],u[3],u[4],u[5],u[6],u[7],u[8],u[9],u[10],u[11],u[12])
            stocks.append(rs);
        self.close(conn)
        return stocks;


if __name__ == '__main__':
    print('start test');

    sqlitedao = SqliteDao('shop');
    sqlitedao.makeTable();
    # newsdao = NewsDAO('shop');
    stocksdao = StocksDAO('shop')


    # # Delete Test
    try:
        # newsdao.delete();
        stocksdao.delete()
        print('OK');
    except:
        print('ErrorCode.E0001');

    # # Insert Test
    # # news1 = NewsVO('구글','www.gogle.com');
    # stocks1 = StockVO('1','삼성전자','1.26','71,300','-2000','-2.73','22,061,786','73,800','74,000','71,300','13.82','9.9','www.samsung.com')
    #
    # # newsdao.insert(news1);
    # stocksdao.insert(stocks1)
    # print('OK');

    # # Select All
    # # result = newsdao.selectall();
    result = stocksdao.selecatall()
    print(result)
    for u in result:
       print(u);


    print('end test');