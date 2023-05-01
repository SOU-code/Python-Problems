'''
Write a program in python to print Floyd's Triangle.
1 
01
101 
0101 
10101
'''
n=int(input())
for i in range(n):
    if((i+1)%2==0):
        constant=0
    else:
        constant=1
    for j in range(i+1):
        print(constant,end='')
        if(constant==0):
            constant=1
        else:
            constant=0
    print()

'''
(OUTPUT)
6
1
01
101
0101
10101
010101
'''