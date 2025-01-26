'''
Author:ALLEN K PHILIP
Description:sum of elements per location in a list
'''

lis1=[]
lis2=[]
n=int(input("enter no: Elements in list:"))
for i in range(0,n):
    num=int(input("enter the element for list1:"))
    lis1.append(num)
    
for i in range(0,n) :
    num2=int(input("enter the element for list2:"))
    lis2.append(num2)
    n=n-1

sum_list=[]
sum_li=0
j=len(lis1)
for k in range(0,j):
    sum_li=int(lis1[k])+int(lis2[k])
    sum_list.append(sum_li)

print(sum_list)
