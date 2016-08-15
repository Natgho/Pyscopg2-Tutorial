#!/usr/bin/python
# -*- coding: utf-8 -*-
# Bi verinin insert islemi

import psycopg2
import sys

con = None

try:
    psycopg2.connect(host='Host_IP_Adress',dbname='Database_name',user='username',password='password')  
    cur = con.cursor()
    cur.execute("INSERT INTO Query")
     
except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
