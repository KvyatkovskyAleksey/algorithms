"""

Code
Testcase
Testcase
Test Result
1493. Longest Subarray of 1's After Deleting One Element
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        left = right = 0
        null_count = 0
        while right < len(nums):
            if nums[right] == 0:
                null_count += 1
                while null_count > 1 and left < right:
                    if nums[left] == 0:
                        null_count -= 1
                    left += 1
            result = max(result, right - left)
            right += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestSubarray([1, 1, 0, 1]) == 3
    assert solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert solution.longestSubarray([1, 1, 1]) == 2
