from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        ans = 0
        for value in frequency.values():
            if value == 1:
                return -1
            ans += math.ceil(value / 3)

        return ans
