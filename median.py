import os
import csv
import unicodedata
DATA = []
FILENAME = 'data.csv'
MEDIAN = ''
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    pass
  try:
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass
  return False
with open(FILENAME, newline='') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    for col in row:
      if isNumber(col):      
        DATA.append(float(col))
DATA = sorted(DATA, key=None, reverse=False)  
if len(DATA)%2 == 0 :
  MEDIAN =  ((DATA[(len(DATA)//2)]) + (DATA[(len(DATA)//2)+1]))/2
else:
  MEDIAN  = DATA[(len(DATA)//2)]
print (MEDIAN)