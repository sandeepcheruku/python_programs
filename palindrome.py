
"""
program to check if a string is a pallindrome 
"""

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

if __name__ == "__main__":
   print "enter a string"
   word = raw_input()
   print is_palindrome(word)
