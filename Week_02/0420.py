# -*- coding: utf-8 -*

# For 4.20
# [299. 猜数字游戏](https://leetcode-cn.com/problems/bulls-and-cows/)
# https://leetcode-cn.com/problems/word-pattern/
# https://leetcode-cn.com/problems/move-zeroes/ (复习)

# Day 6 https://leetcode-cn.com/problems/reverse-only-letters/
# Day 7 https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

class Solution(object):
    # For 4.20

    # [299. 猜数字游戏](https://leetcode-cn.com/problems/bulls-and-cows/)
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        map = {}
        for ch in secret:
            if ch in map:
                map[ch] += 1
            else:
                map[ch] = 1

        A,B = 0,0   
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                if map[guess[i]] == 0:
                    map[guess[i]] += 1
                    B -= 1
                A += 1;
                map[guess[i]] -= 1
            elif guess[i] in map and map[guess[i]] > 0:
                B += 1
                map[guess[i]] -= 1
            
        return '%sA%sB'%(A, B)



if __name__ == "__main__":
    s = Solution()
