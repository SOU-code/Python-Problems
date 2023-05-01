'''Write a python program to determine whether a given number is prime or not.'''


n=int(input())
for i in range(2,n):
    if(n%i==0):
        print(n,"is not a prime number")
        break
else:
    print(n,"is a prime number")

'''
(OUTPUT)
17
17 is a prime number
15
15 is not a prime number
'''