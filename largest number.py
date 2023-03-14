import functools
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i,num in enumerate(nums):
            nums[i]=str(num)
        def compare(n1,n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums=sorted(nums,key=functools.cmp_to_key(compare))
        return str(int("".join(nums)))