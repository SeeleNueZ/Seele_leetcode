class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = n - 1
        ans = 0
        while (i < j):
            if nums[i] + nums[j] < target:
                ans = ans + (j - i)
                i = i + 1
            else:
                j = j - 1

        return ans


