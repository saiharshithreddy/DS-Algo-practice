class Solution:
    def rob(self, nums):
        
        state_1 = state_2 = 0
        max_money_stolen = 0
        
        for money in nums:
            # main logic
            max_money_stolen = max(money + state_2, state_1)
            # update states
            state_1, state_2 = max_money_stolen, state_1
        return max_money_stolen




