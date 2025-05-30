# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    pass


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min_ = 1
        max_ = n

        while True:
            attempt_num = (max_ + min_) // 2
            res = guess(attempt_num)
            if res == 0:
                return attempt_num
            elif res == 1:
                min_ = attempt_num + 1
            else:
                max_ = attempt_num - 1
