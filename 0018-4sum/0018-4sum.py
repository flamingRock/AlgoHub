class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        triplets = []

        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    triplets.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1; r -= 1
                elif sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
        return triplets

        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []

        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            triplets = self.threeSum(nums[i+1:], target - nums[i])
            for item in triplets:
                quadruplets.append([nums[i]] + item)
        
        return quadruplets
            
