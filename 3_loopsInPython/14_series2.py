'''Write a program in python to display the sum of the series [ 9 + 99 + 999 + 9999 ...].'''

n=int(input())
sum=0
num=9
for i in range(n):
    sum+=num
    num=num*10+9
print(sum)

'''
(OUTPUT)
5
111105
'''