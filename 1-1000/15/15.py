class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans=[]
        for i  in range(n-2): # 0 n-3 n-2(j) n-1(k) n-2 ->0~n-3
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            target = 0 - nums[i]
            while(j<k):
                if nums[j]+nums[k] == target:
                    ans.append([nums[i],nums[j],nums[k]])
                    j = j + 1
                    while(j < n-1 and nums[j] == nums[j-1]):
                        j = j + 1
                    k = k - 1
                    while(k > 0 and nums[k]==nums[k+1]):
                        k = k - 1
                elif nums[j]+nums[k] < target:
                    j = j + 1
                    while(j < n-1 and nums[j] == nums[j-1]):
                        j = j + 1
                elif nums[j]+nums[k] > target:
                    k = k - 1
                    while(k > 0 and nums[k]==nums[k+1]):
                        k = k - 1
        return ans

list = [-1,0,1,2,-1,-4]
print(Solution().threeSum(list))