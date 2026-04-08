class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Index is the node, nums[i] tells us whats next
        #Use fast and slow pointers to find cycle

        #After exiting cycle, increrment slow once (since slow is in cycle)
        #Use a diff pointer (slow2) and increment from the start
        #once slow == slow2, we return slow

        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow