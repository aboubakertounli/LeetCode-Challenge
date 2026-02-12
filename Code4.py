class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        pre = [0] * n
        suff = [0] * n       
        pre[0] = 1
        suff[n-1] = 1   
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]    
        ans = [0] * n
        for i in range(n):
            ans[i] = pre[i] * suff[i]
        return ans