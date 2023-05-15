# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = sorted_list = ListNode(0)
        # print("First head = {}, sorted_list = {}".format(head, sorted_list))
        
        while (l1 and l2):
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
            # print("Now head = {}, sorted_list = {}".format(head, sorted_list))
                
        head.next = l1 or l2  # 남은 리스트를 sorted_list 뒤에 할당시켜줌
        
        return sorted_list.next
        