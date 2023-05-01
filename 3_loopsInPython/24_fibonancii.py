'''Write a program in python to display the first n terms of the Fibonacci series.'''
first=0
second=1
n=int(input())
if(n==1):
    print(first,end="")
else:
    print(first,second,end=" ")
for i in range(3,n+1):
    temp=first
    first=second
    second=first+temp
    print(second,end=' ')


'''
(OUTPUT)
9
0 1 1 2 3 5 8 13 21
'''