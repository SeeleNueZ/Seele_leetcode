from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n-2):
            j = n - 2
            k = n - 1
            while (j > i ):
                if j == k:
                    j = j - 1
                elif nums[i] + nums[j] > nums[k]:
                    ans = ans + (k-j)
                    j = j - 1
                elif nums[i] +nums[j] <= nums[k]:
                    k  =  k - 1
        return ans
list = [1,1,3,4]
target = 1
print(Solution().triangleNumber(list))