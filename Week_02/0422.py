# -*- coding: utf-8 -*

# For 4.22
# * [1021. 删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses/)
# * [面试题59 - I. 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/) 暴力解法，时间复杂度 O(kn)

class Solution(object):
    # * [1021. 删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses/)
    def removeOuterParentheses(self, S):
        stack = []
        res = ''

        for ch in S:
            i = 0
            if ch == '(':
                i = 1
                stack.append(ch)
            else:
                stack.pop()

            if len(stack) > i:
                res += ch
        return res

class Solution2(object):
    # * [面试题59 - I. 滑动窗口的最大值](https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/) 
    # 暴力解法，时间复杂度 O(kn)
    def maxSlidingWindow(self, nums, k):
        if k < 2:
            return nums

        res = []
        for i in range(len(nums)-k+1):
            temp = nums[i]
            for j in range(i, i+k):
                if nums[j] > temp:
                    temp = nums[j]
            res.append(temp) 
        return res
