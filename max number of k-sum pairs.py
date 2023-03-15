class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums)==0:
            return 0
        numbers=collections.Counter(nums)
        operations=0
        seen=set()
        for num in numbers:
            if num not in seen and k-num in numbers:
                if num==k-num:
                    operations+=numbers[num]//2
                else:
                    operations+=min(numbers[num],numbers[k-num])
                seen.add(num)
                seen.add(k-num)
        return operations