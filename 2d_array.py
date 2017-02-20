
# initializing a 2-d matrix 


def test (mat):
    print mat

if __name__ == "__main__":
  i, j = 2 , 2;
  matrix = [[0 for x in range(i)] for y in range(j)] 

  for x in range(i):
      for y in range(j):
          print matrix [x][y]

