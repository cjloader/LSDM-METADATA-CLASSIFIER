#!/usr/bin/python
import os
import pymssql
import numpy as np

'''
Use CorpusTuple class to try and find meta data
'''

TOP = 3

uid = os.environ['CORPUS_ID']
pw = os.environ['CORPUS_PW']

conn = pymssql.connect("129.115.236.193", uid, pw);
cursor = conn.cursor()

cursor.execute('select distinct top %d  File_Name from corpus', TOP)
   
csvfiles = cursor.fetchall()


for csv in csvfiles:
   print('csv = %r' % (csv,))
   cursor.execute('select * from corpus where File_Name=%s', csv)
   rows = cursor.fetchall()
   print len(rows)
   #for row in rows:
      #print('row = %r' % (row[0]))
   #   for col in row:
   #      print ('item:%r' % col)

#while row:
#   print("%s" % row[1])
#   row = cursor.fetchone();

conn.close()


