# -*- coding: utf-8 -*

# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        preNonRepeatIndex = 0

        for i in range(1, len(nums)):
            if nums[preNonRepeatIndex] != nums[i]:
                preNonRepeatIndex += 1
                nums[preNonRepeatIndex] = nums[i]
        return preNonRepeatIndex + 1
        
if __name__ == "__main__":
    s = Solution()
    test = [1,1,2]
    n = s.removeDuplicates(test)

    print(test[:n])