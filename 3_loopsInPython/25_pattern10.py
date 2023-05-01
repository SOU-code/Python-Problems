'''
n=3
  1
 121
12321
'''
n=int(input())
for i in range(n):
    for j in range(n-1-i):
        print(' ',end='')
    for k in range(i+1):
        print(k+1,end='')
    for p in range(i,0,-1):
        print(p,end='')
    print()

'''
(OUTPUT)
5
    1
   121
  12321
 1234321
123454321
'''