class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=collections.Counter(nums)
        values=list(count.values())
        values.sort()
        ans=[]
        my_set = set(nums)
        nums = list(my_set)
        for num in nums:
            if values.index(count[num])>=(len(values)-k):
                ans.append(num)
        return ans