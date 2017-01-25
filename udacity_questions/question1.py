
"""
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False.
"""
def anagrams(word):
    if len(word) <= 1:
       return word
    else:
       tmp = []
       for i, letter in enumerate(word):
           for j in anagrams(word[:i]+ word[i+1:]):
               tmp.append(letter + j)
    return tmp

def substrings(word):
    tmp = []
    length = len(word)
    for i in range(length):
        for j in range(i,length):
            if i == 0 and j == len(word)-1:
               print "" 
            else:
               tmp.append(word[i:j+1])
    return tmp 

def question1(s,t):
    substring_list = substrings(s)
    anagram_list = anagrams(t)
    
    for i in anagram_list:
        for j in substring_list:
            if i == j:
               return True

    return False 

if __name__ == "__main__":

    # expected ans : True
    print question1("udacity","ad")
    # expected ans : True
    print question1("python","hno")
    # expected ans : False
    print question1("california","lya")
    
    print "enter the string s:"
    s = raw_input();
    print "enter the string t:"
    t = raw_input();

