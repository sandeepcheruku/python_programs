

# program to find the second lowest value in a array

if __name__ == "__main__":
   scores = []

   n = int(raw_input())
   for _ in range(n):
       name = raw_input()
       score = float(raw_input())
       student = [name, score]
       scores.append(student)

   #print scores
   lowest = scores[0][1]
   second_lowest = scores[0][1]
   flag = 0

   # to find second lowest score 
   for score in scores[1:]:
       i = score[1]
       if i < lowest:
           flag = 1
           second_lowest = lowest
           lowest = i
       elif i > lowest:
            if i < second_lowest or flag == 0:
               flag = 1
               second_lowest = i
   
   #print second_lowest
   #printing all the student names who got second lowest score 
   names = []
   for score in scores:
       i = score[1]
       if i == second_lowest:
          names.append(score[0])

   names.sort()
   for i in names:
      print i 
 
