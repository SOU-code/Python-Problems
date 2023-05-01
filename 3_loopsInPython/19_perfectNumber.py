'''Check whether a given number is a perfect number or not'''
#Perfect number is a positive number which sum of all positive divisors excluding that number is equal to that number. For example 6 is perfect number since divisor of 6 are 1, 2 and 3.  Sum of its divisor is 1 + 2+ 3 = 6

n=int(input())
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(n==sum):
    print(n,"is a perfect")
else:
    print(n,"is not perfect")

'''
(OUTPUT)
28
28 is a perfect
56
56 is not perfect
'''
