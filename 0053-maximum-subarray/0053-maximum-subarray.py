# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         local_max, global_max = 0, nums[0]
#         for num in nums:
#             global_max = max(local_max + num, global_max)
#             local_max = max(0, local_max + num)
#         return global_max


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = 0, nums[0]
        for num in nums:
            # print(f"num = {num}, locol_max = {local_max}, global_max = {global_max}")
            global_max = max(local_max + num, global_max)
            local_max = max(0, local_max + num)
        return global_max