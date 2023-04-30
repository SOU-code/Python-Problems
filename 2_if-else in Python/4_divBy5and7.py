'''Write a python program to check whether a number is divisible by 5 and 7 or not.'''

n=int(input())
if(n%5==0 and n%7==0):
    print(n,"is divisible by both 5 and 7")
else:
    print(n,"is not divisible by both 5 and 7")

'''
(OUTPUT)
35
35 is divisible by both 5 and 7
'''