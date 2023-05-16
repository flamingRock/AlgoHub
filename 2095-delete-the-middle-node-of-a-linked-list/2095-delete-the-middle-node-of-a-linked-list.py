# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        length = 1
        is_null = head
        while is_null.next:
            length += 1
            is_null = is_null.next
            
        mid_index = length // 2
        pre_mid_node = head
        for i in range(mid_index - 1):
            pre_mid_node = pre_mid_node.next
        pre_mid_node.next = pre_mid_node.next.next
        
        return head