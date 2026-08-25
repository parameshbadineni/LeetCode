#1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold


"""
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
Example 2:

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
"""
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
     cumSum=sum(arr[:k-1]) # 0,1
     res=0
     for L in range(len(arr)-k+1):
        cumSum += arr[L+k-1] # arr[2]
        if cumSum/k >= threshold:
           res +=1
        cumSum -=arr[L]
     return res

if __name__ == "__main__":

    sol = Solution()
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    result = sol.numOfSubarrays(arr, k, threshold)
    print(result)
