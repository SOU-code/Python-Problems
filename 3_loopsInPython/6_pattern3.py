'''
n=4
1
22
333
4444
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1,end="")
    print()

'''
(OUTPUT)
8
1
22
333
4444
55555
666666
7777777
88888888
'''