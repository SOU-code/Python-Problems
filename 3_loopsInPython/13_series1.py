'''1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms'''

n=int(input())
sum=0
for i in range(1,n+1):
    sum+=(1/i)
print(sum)

'''
(OUTPUT)
5
2.283333333333333
'''