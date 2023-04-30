'''Boolean Data Type'''
a=True
b=False
print(type(a))
print(type(b))
'''
(OUTPUT)
<class 'bool'>
<class 'bool'>
'''

'''Relational Operators'''
a=10
b=20
print(a>b)
print(a<b)
print(a==b)
print(a>=b)
print(a<=b)

'''
(OUTPUT)
False
True
False
False
True
'''

'''Logical Operators'''
c1=a>10
c2=b>10
r1=c1 and c2
r2=c1 or c2
r3=not(r1)
print(r1)
print(r2)
print(r3)

'''
(OUTPUT)
False
True
True
'''