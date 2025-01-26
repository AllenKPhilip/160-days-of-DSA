"""
Author:ALLEN K PHILIP
Description:Program that let's the user enter to initial height of the ball. show the total distance the ball bounces and total bounce.
"""

height=int(input("Enter the height that ball dropped(in CentiMetre):"))
distance=height
bounce=1
while height>=1:
    height=height*.6
    distance+=height
    bounce+=1
print("Total distance:",distance,"cm")
print("Total bounce:",bounce)
