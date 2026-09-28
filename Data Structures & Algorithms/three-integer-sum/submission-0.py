class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Len = len(nums)
        dict = {}
        

        for num in nums:
            dict[num] = dict.get(num, 0) + 1
    
        res = set()
        for i in range(Len):
            dict[nums[i]] -= 1  # Remove nums[i] from available pool
            
            for j in range(i + 1, Len):
                dict[nums[j]] -= 1  # Remove nums[j] from available pool
                target = -(nums[i] + nums[j])
                
                if dict.get(target, 0) > 0:  # Check if target is still available
                    x = [target, nums[i], nums[j]]
                    x.sort()
                    res.add(tuple(x))
                
                dict[nums[j]] += 1  # Restore nums[j] for next iteration
        
        return list(res)