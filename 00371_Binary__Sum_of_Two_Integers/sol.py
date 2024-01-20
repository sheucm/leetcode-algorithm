import numpy as np
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # Solution1: Use numpy.int64
        if b == 0:
            return a
        return self.getSum(
            np.int32(a ^ b),
            np.int32((a & b) << 1)
        )

        ### Solution 2: Use 32bit mask
        # if b == 0:
        #     return a
        # if b & 0xffffffff == 0:
        #     return a & 0xfffffff
        # return self.getSum((a ^ b), ((a & b) << 1))
