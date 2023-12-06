class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) /3
        integer_counts = Counter(nums)
        valid_numbers = []
        for key, val in integer_counts.items():
            if val > threshold:
                valid_numbers.append(key)
        return valid_numbers