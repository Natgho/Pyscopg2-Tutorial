#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys


con = None
fout = None


try:
     
    psycopg2.connect(host='Host_IP_Adress',dbname='Database_name',user='username',password='password') 
    cur = con.cursor()
    fout = open('accesibility', 'w')
    cur.copy_to(fout, 'accesibility', sep=" ")                        
   

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)

except IOError, e:    
    print 'Error %s' % e   
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

    if fout:
        fout.close() 
