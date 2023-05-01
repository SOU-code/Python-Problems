'''Write a program in python to display the number in reverse order.'''

n=int(input())
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
print(rev)

'''
(OUTPUT)
7456
6547
'''