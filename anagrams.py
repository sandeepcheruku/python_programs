
"""
program generates all possible anagrams of input  
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

if __name__ == "__main__":
    print "enter a word"
    word = raw_input()
    print anagrams(word)

