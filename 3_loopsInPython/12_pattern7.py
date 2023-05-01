'''
n=4 
   1
  2 2
 3 3 3
4 4 4 4
'''

n=int(input())
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for k in range(i+1):
        print(i+1,end=' ')
    print()

'''
(OUTPUT)
6
     1 
    2 2
   3 3 3
  4 4 4 4
 5 5 5 5 5
6 6 6 6 6 6
'''
