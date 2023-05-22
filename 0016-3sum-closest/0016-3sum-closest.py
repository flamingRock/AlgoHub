class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if target == sum:
                    return target
                elif abs(target - sum) < abs(target - closest):
                    closest = sum
                if target < sum:
                    k -= 1
                elif target > sum:
                    j += 1
        return closest