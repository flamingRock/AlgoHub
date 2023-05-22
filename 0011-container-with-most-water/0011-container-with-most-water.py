class Solution:
    # def maxArea(self, height: List[int]) -> int:
        
    #     # length of input array
    #     size = len(height)
        
    #     # two pointers, left init as 0, right init as size-1
    #     left, right = 0, size-1
        
    #     # maximal width between leftmost stick and rightmost stick
    #     max_width = size - 1
        
    #     # area also known as the amount of water
    #     area = 0
        
	# 	# trade-off between width and height
    #     # scan each possible width and compute maximal area
    #     for width in range(max_width, 0, -1):
            
    #         if height[left] < height[right]:
    #             # the height of lefthand side is shorter
    #             area = max(area, width * height[left] )
                
    #             # update left index to righthand side
    #             left += 1
                
    #         else:
    #             # the height of righthand side is shorter
    #             area = max(area, width * height[right] )
                
    #             # update right index to lefthand side
    #             right -= 1
                
    #     return area
    

    # def maxArea(self, height):
    #     L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
    #     for w in range(width, 0, -1):
    #         if height[L] < height[R]:
    #             res, L = max(res, height[L] * w), L + 1
    #         else:
    #             res, R = max(res, height[R] * w), R - 1
    #     return res
    
    def maxArea(self, height):
        leftIndex, rightIndex, width, maxLiter = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[leftIndex] > height[rightIndex]:
                maxLiter, rightIndex = max(w * height[rightIndex], maxLiter), rightIndex - 1
            else:
                maxLiter, leftIndex = max(w * height[leftIndex], maxLiter), leftIndex + 1
        return maxLiter