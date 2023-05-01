'''Write a Python program to display the n terms of odd natural numbers and their sum.'''
n=int(input())
sum=0
i=1
while n>0:
    sum+=i
    i+=2
    n-=1
print(sum)

'''
(OUTPUT)
5
25
'''