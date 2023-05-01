'''Write a python program to find the HCF,LCM of any two numbers '''
a=int(input())
b=int(input())
minimum=min(a,b) #find minimum of two number
for i in range(minimum,0,-1):
    if(a%i==0 and b%i==0):
        hcf=i
        break
print('HCF is:',hcf)
print('LCM is:',(a*b)//hcf)

'''
(OUTPUT)
15
20
HCF is: 5
LCM is: 60
'''