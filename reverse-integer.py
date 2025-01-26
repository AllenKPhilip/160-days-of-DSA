'''
Author:ALLEN K PHILIP
Description:Program to reverse a Integer.
'''

num=int(input("enter the number:"))

def reverse(num):
    newnum=0
    re=0
    while num>0:
        re=num%10
        newnum=newnum*10+re
        num=num//10
    return newnum

if num>0:
    newnum=reverse(num)

else:
    num=-1*num
    newnum=reverse(num)
    newnum=-1*newnum 
print(newnum)
