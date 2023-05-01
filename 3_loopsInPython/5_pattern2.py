'''
n=4
1
12
123
1234
'''

n=int(input())
for i in range(n):
    constant=1
    for j in range(i+1):
        print(constant,end="")
        constant+=1
    print()


'''
(OUTPUT)
6
1
12
123
1234
12345
123456
'''