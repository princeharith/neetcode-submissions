class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #use a hashset to keep track of curr window
        window = set()
        l = 0

        # window = ()

        # [2,1,2]
        #  l   r

        for r in range(len(nums)):
            print(r,l)
            if abs(r-l) > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
            r += 1
        
        return False
        
        