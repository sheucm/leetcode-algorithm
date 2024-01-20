class Solution:
    def reverseBits(self, n: int) -> int:

        # Solution1
        # b = bin(n)[2:].zfill(32)
        # reversed_b = b[::-1]
        # return int(reversed_b, 2)


        # Solution2:
        res = 0
        for _ in range(32):
            first_bit = (n & 1)
            res = (res << 1) | first_bit
            n >>= 1
        return res