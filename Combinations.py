class Solution:
    def find_combination(self,i,nums,comb, ans,k):
        if len(comb) == k:
            ans.append(comb[:])
            return
        if i>=len(nums):
            return
        comb.append(nums[i])
        self.find_combination(i+1,nums,comb,ans,k)
        comb.pop()
        self.find_combination(i+1,nums,comb,ans,k)
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1,n+1)]
        ans = []
        self.find_combination(0, nums,[],ans, k)
        return ans