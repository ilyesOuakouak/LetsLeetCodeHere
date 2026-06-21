class Solution(object):
    def rob(self, nums):
        prev1 = 0
        prev2 = 0

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1


"""
# 1. Initialize our history variables to 0
        # (Imagine two phantom empty houses before the street starts)
        two_steps_back = 0
        one_step_back = 0

        for money in nums:
            # 2. The Choice:
            # Option A: Rob this house (money) + loot from 2 steps back
            # Option B: Skip this house, keep loot from 1 step back
            current = max(money + two_steps_back, one_step_back)
            
            # 3. Slide the window
            two_steps_back = one_step_back
            one_step_back = current
            
        return one_step_back
    """