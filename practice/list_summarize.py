
#using list summarize functionalities to select 3D co-ordinates [i,j,k] while for given inputs x,y,z,n :
#      0 <= i <= x
#      0 <= j <= y
#      0 <= k <= z
#      and i+j+k != n 

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]                               
    print result
