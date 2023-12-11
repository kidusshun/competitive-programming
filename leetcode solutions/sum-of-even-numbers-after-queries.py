class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = 0
        ans = []
        for num in nums:
            if num%2==0:
                evens+=num
        for val, ind in queries:
            if nums[ind]%2==0:
                evens-=nums[ind]
            curr = nums[ind]+val
            if curr%2==0:
                evens+=curr
            nums[ind] = curr
            ans.append(evens)
        return ans