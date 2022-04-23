class bookmarkSql:
    # 종목 담기 DB
    make_bookmarkdb = ''' CREATE  TABLE  IF NOT EXISTS BOOKMARKDB (
        EMAIL TEXT,
        STOCKNAME TEXT,
        URL TEXT
    ) ''';

    insert_bookmarkdb = ''' INSERT  INTO  BOOKMARKDB VALUES (?,?,?) ''';

    delete_bookmarkdb = ''' DELETE  FROM  BOOKMARKDB WHERE EMAIL LIKE ? AND STOCKNAME=? AND URL=?''';

    alldelete_bookmarkdb = ''' DELETE  FROM  BOOKMARKDB ''';

    select_bookmarkdb = ''' SELECT  *  FROM  BOOKMARKDB  WHERE Email LIKE ? AND STOCKNAME=? AND URL=?''';

    selectall_bookmarkdb = ''' SELECT * FROM BOOKMARKDB WHERE EMAIL LIKE ? ''';

    stockname_bookmarkdb = ''' SELECT STOCKNAME FROM BOOKMARKDB WHERE EMAIL LIKE ? ''';
