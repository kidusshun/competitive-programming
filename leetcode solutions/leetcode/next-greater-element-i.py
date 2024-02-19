class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda:-1)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()
                d[val] = num
            stack.append(num)
        return [d[num] for num in nums1]