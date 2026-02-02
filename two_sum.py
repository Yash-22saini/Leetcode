#1.Two_sum
# Return indices of the two numbers that add up to target

from typing import List

class Solution(object):
    def twoSum(self, nums, target):
      
        seen = {}   # number -> index

        for i in range(len(nums)):
            current = nums[i]
            needed = target - current

            if needed in seen:
                return [seen[needed], i]
            else:
                seen[current] = i

# test
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9)) 
