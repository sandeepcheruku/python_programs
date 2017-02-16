


if __name__ == "__main__":
    n = int(raw_input())
    line = raw_input().split()
    line = map(int,line)
    
    largest = line[0]
    second_largest = line[0]
    flag = 0

    for i in line[1:]:
        if i > largest:
            flag = 1
            second_largest = largest 
            largest = i
        elif i < largest:
             if i > second_largest or flag == 0:
                 flag = 1
                 second_largest = i 

    print second_largest

