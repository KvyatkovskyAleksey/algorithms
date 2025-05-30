# https://leetcode.com/problems/string-compression/submissions/1649224415/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: list[str]) -> int:
        current_count = 0
        current_letter = None
        total_chars = len(chars)
        index = 0
        while index < total_chars:
            c = chars.pop(0)
            if current_letter != c:
                if current_count > 1:
                    chars.extend(list(str(current_count)))
                current_count = 1
                current_letter = c
                chars.append(c)
            else:
                current_count += 1
            index += 1
        if current_count > 1:
            chars.extend(list(str(current_count)))
        return len(chars)



if __name__ == '__main__':
    s = Solution()
    assert s.compress(["a","a","b","b","c","c","c"]) == 6
    assert s.compress(["a"]) == 1
    assert s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4