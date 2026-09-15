from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = [0] * 101
        ans = 0

        for num in nums:
            ans += count[num]
            count[num] += 1

        return ans