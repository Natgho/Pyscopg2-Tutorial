#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 Tablo yazma/olusturma/silme islemleri yapılırken bir transaction
 Calisip, yazma islemlerini kontrol etmekte. Commit satiri, yapilan
 Islemlerin database'e uygulanmasini saglamakta. Eger autocommit satiri
 aktiflestirilirse yapilan islem icerisinde otomatik olarak islemler direk
 uygulanir.

'''
import psycopg2
import sys


con = None

try:
     
    psycopg2.connect(host='Host_IP_Adress',dbname='Database_name',user='username',password='password') 
    
    #Eger alttaki satir aktif edilirse otomatik olur yapilan her isşem kommitlenecektir.
    #con.autocommit = True
    
    cur = con.cursor() 

    cur.execute("DROP TABLE IF EXISTS Friends")
    cur.execute("CREATE TABLE Friends(Id serial PRIMARY KEY, Name VARCHAR(10))")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
    
    #con.commit()
       
except psycopg2.DatabaseError, e:
    
    #Eger autocommit aktiflestirilirse bu if silinmeli.
    if con:
        con.rollback()
        
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
