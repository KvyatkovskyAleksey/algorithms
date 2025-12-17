"""
1004. Max Consecutive Ones III
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length

"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        left = 0
        zero_count = 0

        for index, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            result = max(result, index - left + 1)

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2) == 6
    assert (
        solution.longestOnes(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
        )
        == 10
    )
