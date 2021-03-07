'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''

from ListNode import ListNode


class Solution:
    def __init__(self):
        self.sum = 0
        self.index_point = 0
        self.digit = 0
        self.sum_list_node = []

    def createListNode(self, list):
        temp = ListNode()

        for i in reversed(range(0, len(list))):
            if i == len(list) - 1:
                temp = ListNode(list[i])
            else:
                temp = ListNode(list[i], temp)

        # self.printListNode(temp)

        return temp

    def printListNode(self, ln):
        temp = ln
        while True:
            print('ListNode val:', temp.val)

            if temp.next is None:
                break
            else:
                print('ListNode next:', temp.next)
                temp = temp.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ln1 = self.createListNode(l1)
        ln2 = self.createListNode(l2)

        result = ListNode()
        digit = 0

        while True:
            if ln1.val + ln2.val + digit >= 10:
                if ln1.next is None and ln2.next is None:
                    result.val = ln1.val + ln2.val + digit - 10
                    result.next = ListNode(ln1.val + ln2.val + digit - 10)
                    digit = 1
                else:
                    result.val = ln1.val + ln2.val + digit - 10
                    result.next = ListNode()
                    digit = 1
            else:
                result.val = ln1.val + ln2.val
                result.next = ListNode()
                digit = 0

            print('result.val, result.next.val', result.val, result.next.val)

            if ln1.next is None and ln2.next is None:
                break

            if ln1.next is None and ln2.next is not None:
                ln1.next = ListNode()

            elif ln2.next is None and ln1.next is not None:
                ln2.next = ListNode()

            ln1 = ln1.next
            ln2 = ln2.next



            result = result.next

        return result


sln = Solution()
# sln.addTwoNumbers([2,4,3], [5,6,4])
# sln.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9])
# sln.addTwoNumbers([0], [0])
print('result: ')
# sln.printListNode(sln.addTwoNumbers([2, 4, 3], [5, 6, 4]))
sln.printListNode(sln.addTwoNumbers([9, 9, 9, 9, 9, 9, 9],
                                    [9, 9, 9, 9]))
