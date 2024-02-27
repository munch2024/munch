class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        end = len(nums)
        
        for i in range(len(nums)):
            myst = target - nums[i]
            next = i+1
            
            while next < end:
                if myst == nums[next]:
                    return [i, next]
                else:
                    next+=1