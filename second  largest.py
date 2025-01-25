"""
Author:ALLEN K PHILIP
Description:Given an array of positive integers arr[], return the second largest element from the array.
"""

class Solution:
    def getSecondLargest(self, arr):
        l1=arr
        l2=set(l1)
        l3=list(l2)
        l3.sort()
        if len(l3)==1:
            return -1
        else:
            return l3[-2]
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
