# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = second = head
        
        for _ in range(1, k):
            first = first.next
        
        is_null = first
        while is_null.next:
            is_null = is_null.next
            second = second.next
        
        first.val, second.val = second.val, first.val
        
        return head