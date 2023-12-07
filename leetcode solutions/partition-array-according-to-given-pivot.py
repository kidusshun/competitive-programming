class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than = []
        greater_than = []
        equal = []
        for num in nums:
            if num<pivot:
                less_than.append(num)
            elif num==pivot:
                equal.append(num)
            else:
                greater_than.append(num)
        return less_than+equal+greater_than