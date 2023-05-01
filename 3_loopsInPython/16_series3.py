'''Write a program in python to find the sum of the series [ x - x^3 + x^5 + ......].'''

x=int(input())
n=int(input())
sum=0
j=1
for i in range(1,n+1):
    if(i%2==0):
        sum=sum-(x**j)
    else:
        sum=sum+(x**j)
    j+=2
print(sum)

'''
(OUTPUT)
2
5
410
'''