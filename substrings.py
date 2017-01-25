
#Program which generates substrings for a give string

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

if __name__ == "__main__":
    print "enter a string"
    word = raw_input();
    print substrings(word)
