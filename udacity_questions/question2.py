
#Given a string a, find the longest palindromic substring contained in a. 
#Your function definition should look like question2(a)and return a string

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

# calculates the substrings and stores them 
def substrings(word):
    tmp = []
    length = len(word)
    for i in range(length):
        for j in range(i,length):
               tmp.append(word[i:j+1])
    return tmp 

def longest_palindrome(word):
    long_palind = ""
    length = len(long_palind)
    substring_list = substrings(word)
    for i in substring_list:
        if is_palindrome(i):
           if length < len(i):
              long_palind = i
              length = len(i)
    
    return long_palind

if __name__ == "__main__":
   
    # ans : 'godsawIwasdog'
    print longest_palindrome("agodsawIwasdogb")
    # ans : 'godsawIwasdog'
    print longest_palindrome("madam")
    
    #print "enter a string"
    #word = raw_input();

