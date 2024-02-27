# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        tail = temp
        while True:
        
            if list1 is None:
                tail.next = list2
                break
            elif list2 is None:
                tail.next = list1
                break

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
            # print(f'temp val = {curr.val}')
        
        return temp.next