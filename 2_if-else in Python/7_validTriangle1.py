'''Write a python program to input angles of a triangle and check whether triangle is valid or not.'''
a=int(input())
b=int(input())
c=int(input())
if(a+b+c==180):
    print('Triangle is Valid')
else:
    print('Triangle is not Valid')


'''
(OUTPUT)
7_validTriangle1.py"
60
100
90
Triangle is not Valid
7_validTriangle1.py"
60
30
90 
Triangle is Valid
'''