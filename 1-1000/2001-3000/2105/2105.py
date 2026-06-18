class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        l = 0
        l_c = capacityA
        r = n - 1
        r_c = capacityB
        ans = 0
        while (l <= r):
            if (l == r):
                if (r_c > l_c):
                    # 浇水
                    if (r_c < plants[r]):
                        r_c = capacityB
                        ans += 1
                    r_c = r_c - plants[r]
                else:
                    # 浇水
                    if (l_c < plants[l]):
                        l_c = capacityA
                        ans += 1
                    l_c = l_c - plants[l]
                r -= 1
                l += 1
            else:
                # 浇水
                if (l_c < plants[l]):
                    l_c = capacityA
                    ans += 1
                l_c = l_c - plants[l]
                l += 1
                if (r_c < plants[r]):
                    r_c = capacityB
                    ans += 1
                r_c = r_c - plants[r]
                r -= 1
        return ans



