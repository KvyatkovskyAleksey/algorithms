# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_length = len([l for l in s[:k] if l in vowels])
        if max_length == k or len(s) == k:
            return max_length
        current_length = max_length
        for n in range(k, len(s)):

            current_length = current_length + int(s[n] in vowels) - int(s[n - k] in vowels)
            if current_length > max_length:
                max_length = current_length
                if max_length == k:
                    return max_length
        return max_length