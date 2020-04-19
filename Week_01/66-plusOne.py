# -*- coding: utf-8 -*

# https://leetcode-cn.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 < 10:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = 0

        digits.insert(0, 1)
        return digits

if __name__ == "__main__":
    test = [9]
    print(Solution().plusOne(test))