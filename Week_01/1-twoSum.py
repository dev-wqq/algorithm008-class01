# -*- coding: utf-8 -*

# https://leetcode-cn.com/problems/two-sum/

# 最开始做算法的时候，总以为暴力算法不是最佳解法，也没有去写
# 几天学习下来以后，算法就是一个技巧，不会最佳的的可以先将自己会的写出来（暴力也行），后续在慢慢优化

class Solution(object):
    # 利用 哈希表
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        map = {}
        for i, value in enumerate(nums):
            if target - value in map:
                return [map[target-value], i]
            map[value] = i

    # 暴力
    def twoSum2(self, nums, target):

        n = len(nums)
        for i in range(n-1):
            for j in range(n):
                if nums[i] + nums[j] == target:
                    return [i, j]




if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,3,6], 9))

    print(s.twoSum2([2,3,6], 9))
    