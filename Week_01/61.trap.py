# -*- coding: utf-8 -*

# https://leetcode-cn.com/problems/trapping-rain-water/ 
# 使用栈，后面需要多练习才能熟悉 


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        for i in range(len(height)):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                temp = stack[-1]
                stack.pop()
                if len(stack) == 0:
                    break
                distance = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[temp]
                ans += h * distance
            stack.append(i)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    