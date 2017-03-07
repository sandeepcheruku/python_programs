
"""
problem statement:  
Given an array A[] of N integers where each value represents number of chocolates in a packet. 
Each packet can have variable number of chocolates. There are m students, the task is to distribute chocolate packets such that :
1. Each student gets one packet.
2. The difference between the number of chocolates given to the students in packet with maximum chocolates and packet with minimum 
   chocolates is minimum.
Eg:
	Input : A[] = {3, 4, 1, 9, 56, 7, 9, 12} 
        m = 5
	Output: Minimum Difference is 6
	We may pick 3,4,7,9,9 and the output is 9-3 = 6

Link : http://www.practice.geeksforgeeks.org/problem-page.php?pid=1571

"""

if __name__ == "__main__":
    print "hello"

    A = map(int, raw_input().split())
    m = int(raw_input())

    #sorting the array to search for substring whose head-tail value is lowest
    A.sort()
    l = len(A)

    i = 0 
    min_val = A[i+m-1]-A[i]
    low = i
    high = i+m-1
    i += 1
 
    # searching till the end of sorted list and updating at each iteration
    while i+m < l:
        #temp = A[j]-A[i] 
        temp = A[i+m-1]-A[i]
        if temp < min_val:
            min_val = temp
            low  = i
            high = i+m-1
        i += 1
       
    # printing the least diff value possible and the sizes of the packets 
    print "min val is ",min_val
    print "packet sizes and their positions in original list are :"

    i = low
    while i<=high:
        print "\t %d  at %d"% (A[i],i)
        i += 1
        
    
