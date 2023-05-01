'''Write a python program to display the sum of n terms of even natural numbers.'''

n=int(input())
sum=0
i=2
while n>0:
    sum+=i
    i+=2
    n-=1
print(sum)

'''
(OUTPUT)
3
12
'''