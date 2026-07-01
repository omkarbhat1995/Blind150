from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # If the current window is already sorted, the left-most value is the min
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
                
            mid = left + (right - left) // 2
            res = min(res, nums[mid])
            
            # If mid is part of the left sorted portion, search right
            if nums[mid] >= nums[left]:
                left = mid + 1
            # If mid is part of the right sorted portion, search left
            else:
                right = mid - 1
                
        return res