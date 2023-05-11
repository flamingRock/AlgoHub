# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         head = sum_lists = ListNode(0)
#         carry = 0
        
#         while l1 or l2 or carry:
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next
            
#             # list class object is not callable 가 생긴 이유는
#             # sum_lists는 ListNode의 object로써 해당 클래스에 __init__함수가 없기 때문에
#             # 오브젝트에 파라미터를 넣어 저렇게 부를 수 없기 때문
#             sum_lists.next = ListNode(carry % 10)
#             sum_lists = sum_lists.next
#             carry //= 10
            
#         return head.next
    

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = sum_linked = ListNode(0)
        
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            sum_linked.next = ListNode(val)
            sum_linked = sum_linked.next
            
        return head.next
