'''
Write a python program to display Pascal's triangle.
Input number of rows: 5
Expected Output :

        1
      1   1 
    1   2   1 
  1   3   3   1
1   4   6   4   1 
'''
n=int(input())
c=1
for i in range(n):
    for j in range(n-1-i):
        print('  ',end='')
    for k in range(i+1):
        if(i==0 or k==0):
            c=1
        else:
            c=c*(i-k+1)//k
        print(c,end='   ')
    print()

'''
(OUTPUT)
7
            1   
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1
  1   5   10   10   5   1
1   6   15   20   15   6   1
'''