class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = min(height[left], height[right]) * (right - left)
        while (left < right):
            temp = min(height[left], height[right]) * (right - left)
            ans = max(temp, ans)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return ans
