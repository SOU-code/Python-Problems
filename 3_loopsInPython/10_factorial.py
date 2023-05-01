''' Write a python program to calculate the factorial of a given number'''

n=int(input())
fact=1
for i in range(2,n+1):
    fact*=i
print(fact)

'''
(OUTPUT)
5
120
'''