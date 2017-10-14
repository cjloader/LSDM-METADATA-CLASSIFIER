#!/usr/bin/python
import os
import pymssql
import numpy as np
from corpustuple import CorpusTuple
'''
test CorpusTuple class
'''

uid = os.environ['CORPUS_ID']
pw = os.environ['CORPUS_PW']

conn = pymssql.connect("129.115.236.193", uid, pw);
cursor = conn.cursor()

   

cursor.execute( "select * from corpus where File_Name='32503757_0_839030871789776303.csv'")
rows = cursor.fetchall()
#print len(rows)
for row in rows:
   x = CorpusTuple(row)
   print("numspaces:%d" % x.numspaces  )
   print("numdigits:%d" % x.numdigits  )
   print("avglength:%f" % x.avglength  )
   print("numnonnull:%d" % x.numnotnull  )
   print("")
      #print('row = %r' % (row[0]))
   #   for col in row:
   #      print ('item:%r' % col)

#while row:
#   print("%s" % row[1])
#   row = cursor.fetchone();

conn.close()


