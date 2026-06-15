from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0

        pre = [0] * n
        post = [0] * n
        pre[0] = height[0]
        post[n - 1] = height[n - 1]

        for i in range(1, n):
            pre[i] = max(height[i], pre[i - 1])

        for i in range(n - 2, -1, -1):
            post[i] = max(height[i], post[i + 1])

        ans = 0
        for i in range(n):
            ans += min(pre[i], post[i]) - height[i]

        return ans


    def trap1(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0

        x = 0
        y = n - 1

        pre_max = height[x]
        post_max = height[y]

        ans = 0
        while (x < y):
            if pre_max >= post_max:
                ans = ans + (post_max - height[y])
                y = y - 1
                post_max = max(height[y], post_max)
            else:
                ans = ans + (pre_max - height[x])
                x = x + 1
                pre_max = max(height[x], pre_max)

        return ans