# https://leetcode.com/problems/reverse-words-in-a-string/submissions/1628425963/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseWords(self, s: str) -> str:
        reversed = []
        word_length = 0
        s_len = len(s)
        for idx, letter in enumerate(s):
            if letter == ' ' and word_length:
                reversed.insert(0, s[idx-word_length:idx])
                word_length = 0
            elif idx + 1 == s_len:
                word = s[idx-word_length:]
                if word.strip():
                    reversed.insert(0, word.strip())
            elif letter != ' ':
                word_length += 1

        return ' '.join(reversed)

s = Solution()
assert s.reverseWords("the sky is blue") == "blue is sky the", f'{s.reverseWords("the sky is blue")}'

"""
    На самом деле, в python очень простое решение с помощью reverse() 
    или с помощью указателя отрицательного шага среза [::-1]
    def reverseWords(self, s: str) -> str:
        return ' '.join(reverse(s.split()))
"""