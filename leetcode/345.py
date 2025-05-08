# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
# решается двумя указателями - ищем пару гласных и меняем местами

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1

        while left <= right:

            while left < right and s[left] not in vowels:
                left += 1

            while right > left and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
