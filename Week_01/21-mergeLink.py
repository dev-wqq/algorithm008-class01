c

# https://leetcode-cn.com/problems/merge-two-sorted-lists/

# 解题思路：来源于 1 mergeArray，双指针（从前往后移）

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode(-1)
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # cur.next = l1 if l1 is not None else l2
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2

        return head.next