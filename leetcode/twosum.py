# Two Sum Question
# Difficulty: Easy
# Leetcode Problem Section

# The program needs to find the index of the values inside the nums list,
# which can sum together to equalte the value of target
# three cases defined in this problem which can make it smaller 
# in compare to other methods

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        # case 1
        # 