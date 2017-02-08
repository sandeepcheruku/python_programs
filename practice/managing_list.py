
import sys 

if __name__ == '__main__':
   N = int(raw_input())
   lines = []

   # if inputs are given in file format 
   """
   file = open("input.txt","r") 
   N = int (file.readline())
   while 1:
       line = file.readline()
       line = line.rstrip('\n')
       if not line:
           break
       lines.append(line)
   print "read %d lines :"%N
   print lines 
   print " executing the instructions :"
   """
   # if inputs are given in console 
   i = 0
   while i < N:
       line = raw_input()
       lines.append(line)
       i += 1  

   # list to build based on instructions 
   data = []
   for line in lines:
       words = line.split()
       if words[0] == "insert":
          data.insert(int(words[1]),int(words[2]))
       elif words[0] == "print":
           print data
       elif words[0] == "remove":
           data.remove(int(words[1]))
       elif words[0] == "append":
           data.append(int(words[1]))
       elif words[0] == "sort":
           data.sort()
       elif words[0] == "pop":
           data.pop()
       elif words[0] == "reverse":
           data.reverse()
   
