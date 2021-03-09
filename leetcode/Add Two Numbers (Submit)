# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.sum = 0
        self.index_point = 0
        self.digit = 0
        self.sum_list_node = []

    def createListNode(self, m_list):
        temp = ListNode()
        for i in reversed(range(0, len(m_list))):
            if i == len(m_list) - 1:
                temp = ListNode(m_list[i])
            else:
                temp = ListNode(m_list[i], temp)

        # self.printListNode(temp)

        return temp

    def printListNode(self, ln):
        temp = ln
        result_list_node = []
        while True:
            result_list_node.append(temp.val)
            if temp.next is None:
                break
            else:
                temp = temp.next
        return result_list_node
    
    def listNode2list(self, ln):
        temp = ln
        m_list = []
        while True:
            m_list.append(temp.val)
            if temp.next is None:
                break
            else:
                temp = temp.next
        return m_list

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1, l2)
        max_len = max(len(self.listNode2list(l1)), len(self.listNode2list(l2)))
        result_ln = [0 for _ in range(0, max_len)]

        ln1 = self.createListNode(self.listNode2list(l1))
        ln2 = self.createListNode(self.listNode2list(l2))
        result = self.createListNode(result_ln)

        digit = 0

        while True:

            if ln1.next is None and ln2.next is None:
                if ln1.val + ln2.val + digit >= 10:
                    result.val = ln1.val + ln2.val + digit - 10
                    digit = 1
                    result.next = ListNode(digit)
                    self.sum_list_node.append(result)
                else:
                    result.val = ln1.val + ln2.val + digit
                    result.next = None
                    self.sum_list_node.append(result)
                break

            if ln1.next is None and ln2.next is not None:
                ln1.next = ListNode()

            elif ln2.next is None and ln1.next is not None:
                ln2.next = ListNode()

            if ln1.val + ln2.val + digit >= 10:
                result.val = ln1.val + ln2.val + digit - 10
                digit = 1
                result.next = ListNode(ln1.next.val + ln2.next.val + digit)
            else:
                result.val = ln1.val + ln2.val + digit
                digit = 0
                result.next = ListNode(ln1.next.val + ln2.next.val)

            # print('result.val, result.next.val', result.val, result.next.val)
            self.sum_list_node.append(result)

            ln1 = ln1.next
            ln2 = ln2.next
            result = result.next

        return self.sum_list_node[0]
