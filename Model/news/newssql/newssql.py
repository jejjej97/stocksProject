class NewsSql:

    # 유저 DB
    make_newsdb = ''' CREATE  TABLE  IF NOT EXISTS NEWS_DB (
        TITLE  TEXT,
        LINK  TEXT,
        PRESS TEXT,
        DTIME DATE
    ) ''';
    insert_newsdb = '''  
             INSERT INTO  NEWS_DB (TITLE, LINK, PRESS, DTIME) VALUES  (?,?,?,?) 
         ''';

    delete_newsdb = '''  
             DELETE   FROM  NEWS_DB
         ''';
    select_newsdb = '''
             SELECT * FROM NEWS_DB WHERE TITLE LIKE ?
         '''
    selectall_newsdb = ''' SELECT * FROM NEWS_DB ''';
