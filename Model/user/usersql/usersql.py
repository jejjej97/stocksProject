class userSql:
    # 유저 DB
    make_userdb = ''' CREATE  TABLE  IF NOT EXISTS USER_DB (
        Email  TEXT  PRIMARY KEY,
        Password  TEXT,
        Name TEXT
    ) ''';
    insert_userdb = ''' INSERT  INTO  USER_DB VALUES (?,?,?) ''';
    update_userdb = ''' UPDATE  USER_DB  SET  Password=?,  Name=?  WHERE  Email=? ''';
    delete_userdb = ''' DELETE  FROM  USER_DB  WHERE  Email=? AND Password=? AND Name=?''';
    select_userdb = ''' SELECT  Email, Password, name  FROM  USER_DB  WHERE Email=? ''';
    selectall_userdb = ''' SELECT  Email, Password, name FROM USER_DB ''';
