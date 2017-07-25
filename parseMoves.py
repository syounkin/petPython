from __future__ import print_function
import re
filename = 'chess.pgn'

# Make sure file gets closed after being iterated
with open(filename, 'r') as f:
   lines = f.readlines()

moveTimeList = []

for line in lines:

   line = line.replace("{[","")
   line = line.replace("]}","")
   line = line.replace(":",".")
   
   lineVec = line.split(' ')
   whiteDate,whiteTime = lineVec[2].split(',')
   blackDate,blackTime = lineVec[5].split(',')
   moveTimeList.append(whiteDate+"."+whiteTime)
   moveTimeList.append(blackDate+"."+blackTime)
   
print(moveTimeList)
