# very similar to 3sum but uses two initialised values 
# still uses left, right algotithim 

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        quadruplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:   # skips duplicates for i 
                continue
            for j in range(i + 1, len(nums)):       # skips duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                        # skips left / right duplicates
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
    
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets
        
