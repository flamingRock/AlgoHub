from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        # op, cl, stack = "({[", {')':'(', '}':'{',']':'['}, []
        op = {'(', '{','['}   # dict가 list보다 빠르다 확실히
        cl = {')':'(', '}':'{',']':'['}
        stack = []
        
        for c in s:
            if c in op:
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != cl[c]:
                return False
        
        return not stack
        
        
# 확실한 이유는 모르겠지만 여기서 queue.LifoQueue를 쓰면 많이 느리다  
#     def isValid(self, s: str) -> bool:
#         stack = LifoQueue()
#         op = "({["
#         cl = {')':'(', '}':'{', ']':'['}
#         for c in s:
#             if c in op:
#                 stack.put(c)
#             elif stack.empty() or stack.get() != cl[c]:
#                 return False
        
#         return stack.empty()
        
        