'''
n=9
    *
   *** 
  *****
 *******
********* 
 *******
  *****
   ***
    * 
'''

n=int(input())
odd=(n//2)+1
even=n//2
for i in range(odd):
    for j in range(odd-1-i):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()
for i in range(even):
    for j in range(i+1):
        print(' ',end='')
    for k in range((even-i)*2-1):
        print('*',end='')
    print()

'''
(OUTPUT)
11
     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
'''