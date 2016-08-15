#!/usr/bin/python
# -*- coding: utf-8 -*-
# Baglanilan Tablonun kolon adlarini erisim
import psycopg2
import sys


con = None

try:
     
    psycopg2.connect(host='Host_IP_Adress',dbname='Database_name',user='username',password='password')  
    
    cur = con.cursor()
 
    cur.execute('Sql_Query')
    
    col_names = [cn[0] for cn in cur.description]
    
    rows = cur.fetchall()
    
    #print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])
    for col_name in col_names:
        print col_name + "-",
    
   

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
