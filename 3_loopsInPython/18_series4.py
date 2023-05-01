'''Write a program in python to find the sum of the series 1 +11 + 111 + 1111 + .. n terms.'''

n=int(input())
constant=1
sum=0
for i in range(n):
    sum+=constant
    constant=constant*10+1
print(sum)

'''
(OUTPUT)
5
12345
'''