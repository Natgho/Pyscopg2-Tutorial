#!/usr/bin/python
# -*- coding: utf-8 -*-
#Verinin direk dizin icerisine alma yontemi
import psycopg2
import sys

con = None

try:
    con = psycopg2.connect(host='Host_IP_Adress',dbname='Database_name',user='username',password='password') 
    cur = con.cursor()
    cur.execute("SqlQuery")
    icerik = cur.fetchall()
    
    for satir in icerik:
        #print satir
        print satir[0], satir[1], satir[2]
     

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
