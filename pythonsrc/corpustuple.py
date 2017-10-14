import re

'''
This class will take a row as input which is a row from corpus, and
determine all the different attrs to be used in the vector for this particular row 
We can add more attrs here, which will have to be taken to account with the number of
dimension our vectors are in meta_detector.py
'''

class CorpusTuple():
   def __init__(self, row):
      self.row = row
      self.numspaces = 0
      self.numdigits = 0
      self.numnotnull = 0
      self.avglength = 0.0
      self.__countnotnull()
      self.__countspaces()
      self.__countdigits()
      self.__countavglength()


   def __countnotnull(self):
      itercols = iter(self.row)
      next(itercols) #skip csv col
      for col in itercols:
         if col is not None:
            self.numnotnull += 1


   def __countspaces(self):
      itercols = iter(self.row)
      next(itercols) #skip csv col
      for col in itercols:
         if hasattr(col, 'count'):
            self.numspaces += col.count(' ');

   def __countdigits(self):
      itercols = iter(self.row)
      next(itercols) #skip csv col
      for col in itercols:
         if col is not None:
            try:
               self.numdigits += len(re.findall("\d", col))
            except TypeError:
               try:
                  self.numdigits += len(re.findall("\d", str(col)))
               except Exception as err:
                  print("tried and failed to count digits for %r:%s" % (col, err))



      #print("total %d" % total)

   def __countavglength(self):
      total = 0
      itercols = iter(self.row)
      next(itercols) #skip csv col
      for col in itercols:
         if col is not None:
            try:
               total += len(col)
            except TypeError:
               try:
                  total += len(str(col))
               except Exception as err:
                  print("tried and failed to get length of %r:%s" % (col, err))

      self.avglength = float(total) /  self.numnotnull





