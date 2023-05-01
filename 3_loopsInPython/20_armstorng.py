'''Write a python program to check whether a given number is an Armstrong number or not.'''
#When the sum of the cube of the individual digits of a number is equal to that number, the number is called Armstrong number. For Example 153 is an Armstrong number because 153 = 13+53+33.

n=int(input())
temp=n
sum=0
while temp>0:
    r=temp%10
    temp=temp//10
    sum=sum+r**3
if(sum==n):
    print(n,"is a armstrong Number")
else:
    print(n,"is not a armstrong Number")

'''
(OUTPUT)
370
370 is a armstrong Number
143
143 is not a armstrong Number
'''