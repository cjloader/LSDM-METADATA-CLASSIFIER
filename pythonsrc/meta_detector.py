#!/usr/bin/python
import os
import pymssql
import numpy as np
from corpustuple import CorpusTuple
from scipy.cluster.vq import vq, kmeans, whiten

'''
Use CorpusTuple class to try and find meta data
'''

TOP = 30

uid = os.environ['CORPUS_ID']
pw = os.environ['CORPUS_PW']

conn = pymssql.connect("129.115.236.193", uid, pw);
cursor = conn.cursor()

cursor.execute('select distinct top %d  File_Name from corpus', TOP)
   
csvfiles = cursor.fetchall()
csvstring = "";

itercsvfiles = iter(csvfiles)
csv = next(itercsvfiles)
csvstring += "File_Name='" + str(csv[0]) + "'"

for csv in itercsvfiles:
   csvstring += " OR File_Name='" + str(csv[0]) + "'"


querystring = "select * from corpus where " +  csvstring

cursor.execute(querystring)
rows = cursor.fetchall()
numberofrows = len(rows)

iterrows = iter(rows)
firstrow = next(iterrows)

firstcorpustuple = CorpusTuple(firstrow)
numattrs = len(vars(firstcorpustuple)) - 1 

kmeansMat = np.zeros( (numberofrows, numattrs) )

firstdict = vars(firstcorpustuple)
del(firstdict['row'])
for idx, dictitem in enumerate(firstdict):
   kmeansMat[0][idx] = firstdict[dictitem]


for col,row in enumerate(iterrows):
   corpustuple = CorpusTuple(row)
   corpustupledict = vars(corpustuple)
   del(corpustupledict['row'])
   for idx,dictitem in enumerate(corpustupledict):
      kmeansMat[col+1][idx] = corpustupledict[dictitem]


whitened = whiten(kmeansMat)
code_book = kmeans(whitened ,2)[0]

code = vq(whitened, code_book)[0]
cluster0 = open('cluster0.txt', 'w');
cluster1 = open('cluster1.txt', 'w');
for idx, c in enumerate(code):
   if c == 0:
      cluster0.write(str(rows[idx]) + "\n")
   else:
      cluster1.write(str(rows[idx]) + "\n")




conn.close()


