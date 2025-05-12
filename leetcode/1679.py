# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        locs = {}
        for num in nums:
            if num not in locs:
                locs[num] = 1
            else:
                locs[num] += 1
        answer = 0
        for num, times in locs.items():
            find = k - num
            if find > num:
                continue
            if find == num:
                answer += times // 2
            elif find in locs:
                answer += min(locs[find], times)
        return answer