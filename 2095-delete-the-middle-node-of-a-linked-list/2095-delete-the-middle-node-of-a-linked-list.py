# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#       # 중간 값은 다음다음과 다음의 차이에 있다''를 사용하는 방식
#         if not head.next:
#             return head.next
        
#         fast, slow = head.next.next, head
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         slow.next = slow.next.next
#         return head
        
        
      # 단순히 중간 index를 구해 해당 Node를 delete하는 방식
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
