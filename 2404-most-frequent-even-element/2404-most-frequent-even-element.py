class Solution:
    def mostFrequentEven(self, nums):
        count = {}

        for num in nums:
            if num % 2 == 0:
                count[num] = count.get(num, 0) + 1

        ans = -1
        freq = 0

        for num in count:
            if count[num] > freq:
                freq = count[num]
                ans = num
            elif count[num] == freq and num < ans:
                ans = num

        return ans