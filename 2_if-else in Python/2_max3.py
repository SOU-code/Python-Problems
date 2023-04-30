'''Write a python program to find maximum between three numbers.'''
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print(a,"is maximum")
elif(b>a and b>c):
    print(b,"is maximum")
else:
    print(c,"is maximum")

'''
(OUTPUT)
5    
7
3
7 is maximum
'''