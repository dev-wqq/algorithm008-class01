# -*- coding: utf-8 -*

# https://leetcode-cn.com/problems/merge-sorted-array/

# 1. 暴力解法，合并后排序
# 2. 双指针（从后往前移）


class Solution(object):
    # 暴力
    def merge1(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)
        # for test
        print(nums1)

    # 最佳
    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p2 = n - 1
        p = m + n -1 
        while(p1 >= 0 and p2 >= 0):
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1  
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        nums1[:p2+1] = nums2[:p2+1]

        # for test
        print(nums1)

    

if __name__ == "__main__":
    s = Solution()

    s.merge1([2,2,3,0,0,0],3,[0,1,6],3)

    s.merge2([2,2,3,0,0,0],3,[0,1,6],3)
