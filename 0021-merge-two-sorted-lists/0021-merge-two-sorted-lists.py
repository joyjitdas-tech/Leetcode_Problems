# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        new = None
        tail = None

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next

            if new is None:
                new = node
                tail = new
            else:
                tail.next = node
                tail = tail.next
        while list1 is not None:
            node = ListNode(list1.val)
                


            if new is None:
                new = node
                tail = new
            else:
                tail.next = node
                tail = tail.next
            list1 = list1.next
        while list2 is not None:
            node = ListNode(list2.val)
                


            if new is None:
                new = node
                tail = new
            else:
                tail.next = node
                tail = tail.next
            list2 = list2.next

        return new