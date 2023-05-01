'''Write a python program to check whether a number is a Strong Number or not.'''
'''If sum of factorial of digits is equal to original number then it is Strong number'''
n=int(input())
temp=n
sum=0
while(n>0):
    r=n%10
    n=n//10
    tempSum=1
    for i in range(1,r+1):
        tempSum*=i
    sum+=tempSum
if(sum==temp):
    print(temp,'is a strong number')
else:
    print(temp,'is not a strong number')

'''
(OUTPUT)
153
153 is not a strong number
145
145 is a strong number
'''