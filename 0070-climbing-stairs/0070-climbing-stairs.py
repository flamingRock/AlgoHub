# Top down + memorization (dictionary) 
class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}
        
    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

# DP top-down => TLE(Time Limit Exceeded)
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         else :
#             return self.climbStairs(n-1) + self.climbStairs(n-2)


# DP bottom-up, memorization
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         step_nums = [1, 1]
        
#         for i in range(2, n+1):
#             step_nums.append(step_nums[i-1] + step_nums[i-2])
        
#         return step_nums[n]
        