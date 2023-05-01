'''Write a C program that displays the n terms of square natural numbers and their sum.
1 4 9 16 ... n Terms'''

n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i*i
print(sum)

'''
5
55
'''