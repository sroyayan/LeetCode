class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}

        for digit in str(n):
            freq[digit] = freq.get(digit, 0) + 1

        score = 0

        for digit in freq:
            score += int(digit) * freq[digit]

        return score