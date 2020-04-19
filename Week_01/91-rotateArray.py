# -*- coding: utf-8 -*

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k%len(nums) == 0:
            return
            
        k = k%len(nums)
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]