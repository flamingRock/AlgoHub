# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # LL를 array로 만들면서 length 재기
        arr = []
        cur, length = head, 0
        
        while cur:
            arr.append(cur)
            cur, length = cur.next, length + 1
        
        # 두 pointer(left, right)로 좌우 번갈아가면서 LL에 넣기
        # 마지막 노드는 last로
        left, right = 0, length - 1
        last = head
        
        while left < right:
            arr[left].next = arr[right]
            left += 1
            
            if left == right:
                last = arr[right]
                break
            
            arr[right].next = arr[left]
            right -= 1
            
            last = arr[left]
        
        
        last.next = None