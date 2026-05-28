from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = j + 1
                l = n - 1

                while (k < l):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k = k + 1
                        while (nums[k] == nums[k - 1] and k < n - 1):
                            k = k + 1
                        l = l - 1
                        while (nums[l] == nums[l + 1] and l > j):
                            l = l - 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k = k + 1
                        while (nums[k] == nums[k - 1] and k < n - 1):
                            k = k + 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l = l - 1
                        while (nums[l] == nums[l + 1] and l > j):
                            l = l - 1
        return ans
list = [-2,-1,-1,1,1,2,2]
target = 0
print(Solution().fourSum(list,target))