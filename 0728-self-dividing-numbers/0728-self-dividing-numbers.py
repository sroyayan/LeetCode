class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst = []

        for i in range(left, right + 1):
            is_self_dividing = True
            for digit in str(i):
                d = int(digit)
                if d == 0 or i % d != 0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                lst.append(i)

        return lst