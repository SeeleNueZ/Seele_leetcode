from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0]+nums[1]+nums[n-1]
        x = abs(ans-target)
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while(j<k):
                ans_t = nums[i]+nums[j]+nums[k]
                y = ans_t-target
                x_t = abs(y)
                if x_t < x :
                    x = x_t
                    ans = ans_t
                if y < 0:
                    j = j + 1
                elif y > 0:
                    k = k - 1
                elif y == 0:
                    return ans_t
        return ans

list = [-1,2,1,-4]
target = 1
print(Solution().threeSumClosest(list,target))