'''Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.'''
a=int(input())
b=int(input())
c=int(input())
if(a==b and b==c):
    print('Triangle is equilateral')
elif(a==b or b==c or c==a):
    print('Triangle is isosceles')
else:
    print('Triangle is scalene')

'''
(OUTPUT)
Python/9_triangleTypes.py"
10
10
10
Triangle is equilateral
10
6
6
Triangle is isosceles
3
5
4
Triangle is scalene
'''