
#import numpy as np

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    #print np.mean(student_marks[query_name])
    #print round(sum(student_marks[query_name])/3,2)
    print "%.2f " % (sum(student_marks[query_name])/3)
