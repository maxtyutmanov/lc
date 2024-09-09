class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            # skip the first house and solve for the rest
            wo_first = self.rob_chain(nums[1:])
            # now don't skip the first house
            wo_last = self.rob_chain(nums[:-1])
            return max(wo_first, wo_last)

    def rob_chain(self, nums: List[int]) -> int:
        n = len(nums)
        d = [[0] * 2] * n
        # d[i][0] - amount if i-th house is not robbed
        # d[i][1] - amount if i-th house is robbed

        d[0][0] = 0
        d[0][1] = nums[0]

        for i in range(1, n):
            # if we don't rob then either previous house was robbed or it wasn't robbed - both options are available
            if_not_rob = max(d[i - 1][1], d[i - 1][0])
            # if we do rob, then the only option left is previous house was not robbed
            if_rob = nums[i] + d[i - 1][0]
            d[i][0] = if_not_rob
            d[i][1] = if_rob
        
        return max(d[n - 1][0], d[n - 1][1])