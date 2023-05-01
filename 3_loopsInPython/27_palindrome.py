'''Write a python program to check whether a number is a palindrome or not.'''
n=int(input())
temp=n
rev=0
while n>0:
    r=n%10
    n=n//10
    rev=rev*10+r
if(rev==temp):
    print(temp,"is a palindrome number")

'''
(OUTPUT)
1345431
1345431 is a palindrome number
'''