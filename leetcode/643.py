# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = sum(nums[:k])
        current_value = max_avg
        for n in range(1, len(nums) - k + 1):
            current_value = current_value - nums[n - 1] + nums[n + k - 1]
            if current_value > max_avg:
                max_avg = current_value
        return max_avg / k

if __name__ == '__main__':
    s = Solution()
    assert s.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75