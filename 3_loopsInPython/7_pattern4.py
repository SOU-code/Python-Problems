'''
n=4
1
2 3
4 5 6
7 8 9 10
'''
n=int(input())
constant=1
for i in range(n):
    for j in range(i+1):
        print(constant,end=" ")
        constant+=1
    print()

'''
(OUTPUT)
5
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''