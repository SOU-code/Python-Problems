'''Write a python program to input all sides of a triangle and check whether triangle is valid or not.'''
a=int(input())
b=int(input())
c=int(input())
if(a+b>c and b+c>a and c+a>b):
    print('Triangle is Valid')
else:
    print('Triangle is not Valid')


'''
(OUTPUT)
10
3
2
Triangle is not Valid

10
5
6
Triangle is Valid
'''