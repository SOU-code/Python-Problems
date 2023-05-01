'''Write a python program to convert a binary number into a decimal number without using array, function and while loop.'''
n=int(input())
sum=0
count=0
while(n>0):
    r=n%10
    n=n//10
    if(r!=0):
        sum+=2**count
    count+=1
print(sum)

'''
(OUTPUT)
1010101
85
'''