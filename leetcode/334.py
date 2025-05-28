# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = middle = 2 ** 31
        for num in nums:
            # this way we search left, it will be smallest, because if it's higher, we get num
            if left >= num:
                left = num
            # if next num higher of smaller, we can set middle
            elif middle >= num:
                middle = num
            # if num higher than both left and middle - get it
            else:
                return True
        return False

if __name__ == '__main__':
    f = Solution().increasingTriplet
    assert f([1,2,3,4,5]) == True
    assert f([1,6,2,5,1]) == True
    assert f([3,3,3,2,0,1,1]) == False