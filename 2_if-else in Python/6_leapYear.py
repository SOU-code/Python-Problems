'''Write a python program to check whether a year is leap year or not.'''

year=int(input())
if((year%4==0 and year%100!=0) or year%400==0):
    print(year,"Is a leap Year")
else:
    print(year,"IS not a leap year")

'''
(OUTPUT)
6_leapYear.py"
2000
2000 Is a leap Year
6_leapYear.py"
2012
2012 Is a leap Year
6_leapYear.py"
2013
2013 IS not a leap year
6_leapYear.py"
1900
1900 IS not a leap year
'''