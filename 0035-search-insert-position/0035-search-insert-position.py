class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        highest = len(nums) - 1 
        lowest = 0

        while lowest <= highest:
            middle = (highest + lowest)//2
            guess = nums[middle]

            if guess == target:
                return middle
            
            if guess > target:
                highest = middle - 1
            
            else:
                lowest = middle + 1

        return lowest