# -*- coding: utf-8 -*

# https://leetcode-cn.com/problems/move-zeroes/

class Solution(object):
    # 时间复杂度 O(n)
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1
        
        # for test
        print(nums)

if __name__ == "__main__":
    test_case = [0,1,0,3,12]
    Solution().moveZeroes(test_case)

    
