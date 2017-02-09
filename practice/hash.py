
if __name__ == '__main__':
   n = int(raw_input())
   # reading the input and storing it as a list 
   integer_list = map(int, raw_input().split())
   # converting input from list to tuple 
   t = tuple(integer_list) 
   # printing the hash of tuple 't'
   print hash(t)
   
