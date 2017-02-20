
"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions.
It is : 0,1,1,2,3,5,......  for ( n=0,n=1,n=2,n=3,......) 
"""

# using recursion
# time complexity : O(2^n)
# space complexity : O(n)
def get_fib(position):
    if position == 0:
       return 0  
    elif position == 1:
       return 1 
    else:
       return (get_fib(position-1) + get_fib(position-2))


# using memorization technique 
# time complexity : O(n) (as we are memorizing calculated values and no need to call those values again using recursion)
# space complexity : O(n)

def print_fib(num):
    mem = [0 for x in range(num+1)]
    return fib_mem(mem,num)
    
def fib_mem(mem,num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif mem[num] == 0:
         mem[num] = fib_mem(mem,num-1) + fib_mem(mem,num-2)
        
    return mem[num]

if __name__ == "__main__":
 
  """
  # Test cases
  print get_fib(0)
  print get_fib(1)
  print get_fib(2)
  print get_fib(3)
  """
  
  print print_fib(0)
  print print_fib(1)
  print print_fib(2)
  print print_fib(3)
  print print_fib(4)
  print print_fib(5)
