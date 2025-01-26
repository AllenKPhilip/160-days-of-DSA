'''
Author:ALLEN K PHILIP
Description:The median of the two sorted arrays.
'''


n=int(input("enter the No: Elements in 1st list:"))
list1=[]
for i in range(0,n):
    num=int(input("enter the elements:"))
    list1.append(num)

m=int(input("enter the No: Elements in 2st list:"))
list2=[]
for k in range(0,m):
    ele=int(input("enter the elements:"))
    list2.append(ele)

list_main=list1+list2
list_main.sort()
y=len(list_main)
sum=0
for i in list_main:
    sum=sum+i
median=sum/y
print(median)
