#!/usr/bin/python
# -*- coding: utf-8 -*-
# DB'den sadece 1 satir veri cekmeyi saglar

import psycopg2
import sys


con = None

try:
     
    psycopg2.connect(host='Host_IP_Adress',dbname='Database_name',user='username',password='password') 
    
    cur = con.cursor()     
    cur.execute("Sql Query")

    row = cur.fetchone()
    
    if row == None
        print "Veri cekilemedi."
        break
                
    print row[0], row[1], row[2]

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
