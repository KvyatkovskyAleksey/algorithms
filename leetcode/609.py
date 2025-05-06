# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        free_cell_count = 0
        flowers = 0
        flowerbed_len = len(flowerbed)
        for idx, cell in enumerate(flowerbed):
            if idx == 0:
                free_cell_count += 1
            if idx == flowerbed_len - 1:
                free_cell_count += 1
            if not cell:
                free_cell_count += 1
            else:
                free_cell_count = 0
            if free_cell_count >= 3:
                free_cell_count = 1
                flowers += 1
                if flowers == n:
                    return True
        return False

s = Solution()
assert s.canPlaceFlowers([1,0,0,0,0,0,1], 2) == True
assert s.canPlaceFlowers([1,0,0,0,1], 1) == True
assert s.canPlaceFlowers([0], 1) == False
assert s.canPlaceFlowers([1, 0, 1], 0) == True
assert s.canPlaceFlowers([0, 0, 1], 1) == True
assert s.canPlaceFlowers([1, 0, 0], 1) == True