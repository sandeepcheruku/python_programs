
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

# this fuc generates all possible anagrams and substrings and verifies them accross each one of them 
def question1_1(s,t):
    substring_list = substrings(s)
    anagram_list = anagrams(t)
    
    for i in anagram_list:
        for j in substring_list:
            if i == j:
               return True

    return False 

# this program verfies by measuring the frequencies of the substrings 
def question1(s,t):
     
    freq_p = [0] * 256
    freq_t = [0] * 256
    len_t = len(s)
    len_p = len(t)

    if len_p > len_t:
       return False 

    for i in range(len_p):
        freq_t[ord(s[i])] +=1
        freq_p[ord(t[i])] +=1

    for i in range(len_p,len_t):
        if freq_p == freq_t:
           return True
        freq_t[ord(s[i-len_p])] -=1
        freq_t[ord(s[i])] +=1
    
    if freq_p == freq_t:
       return True
    else:
       return False

if __name__ == "__main__":

    print question1("udacity","ad")
    # expected ans : True
    print question1("python","hno")
    # expected ans : False
    print question1("california","lya")
    
    print "enter the text string on which you wish to search 's':"
    s = raw_input();
    print "enter the substring t whose of whose anagrams you wish to verify 't':"
    t = raw_input();
    print question1(s,t)

