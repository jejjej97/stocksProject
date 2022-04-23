class StocksSql:

    make_stocksdb = '''CREATE TABLE IF NOT EXISTS STOCKSDB (
                RANK TEXT,
                STOCK TEXT,
                SRATE TEXT,
                NPRICE TEXT,
                YRATE TEXT,
                UPDOWNRATE TEXT,
                TAMOUNT TEXT,
                MPRICE TEXT,
                HIGH TEXT,
                LOW TEXT,
                PER TEXT,
                ROE TEXT,
                LINK TEXT
                ) ''';

    insert_stocksdb = '''
                INSERT INTO STOCKSDB (RANK, STOCK, SRATE, NPRICE, YRATE, UPDOWNRATE, TAMOUNT, MPRICE, HIGH, LOW, PER, ROE, LINK)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''';

    delete_stocksdb = '''  
             DELETE   FROM  STOCKSDB
         ''';

    selectall_stocksdb = '''SELECT * FROM STOCKSDB''';