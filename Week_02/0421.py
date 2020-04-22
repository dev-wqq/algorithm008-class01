
# -*- coding: utf-8 -*

# For 4.21
# [350. 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)
# [392. 判断子序列](https://leetcode-cn.com/problems/is-subsequence/)
# [面试题 17.09. 第 k 个数](https://leetcode-cn.com/problems/get-kth-magic-number-lcci/)

## TODO:完成第一遍刷题，待看完视频后，重新做题

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if(len(nums1) > len(nums2)):
            nums1, nums2 = nums2, nums1
        
        map = {}
        for i in nums1:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        list = []
        for i  in nums2:
            if i in map and map[i] > 0:
                list.append(i)
                map[i] -= 1
        return list


class Solution2(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        ps, pt = 0, 0

        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                if ps == len(s):
                    return True
            pt += 1 
        
        return False


class Solution3(object):
    def getKthMagicNumber(self, k):
        """
        :type k: int
        :rtype: int
        """

        res = [1] * k
        i3, i5, i7 = 0,0,0

        # res[0] = 1
        for i in  range(1, k):
            res[i] = min(res[i3] * 3, res[i5] * 5, res[i7] * 7)

            if res[i] == res[i3] * 3:
                i3 += 1
            if res[i] == res[i5] * 5:
                i5 += 1
            if res[i] == res[i7] * 7:
                i7 += 1

        return res[k-1]


if __name__ == "__main__":
    






        















