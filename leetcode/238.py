# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        # произведением числа будет произведение всех чисел слева на произведение всех чисел справа
        # поэтому в 2 захода мы можем пройти сначала влево (и беря произведение предыдущего элемента)
        # и вправо - используя следующий элемент, а затем перемножить получившиеся произведения

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer