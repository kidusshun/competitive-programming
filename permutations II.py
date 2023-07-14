from collections import Counter
class Solution:
    def find_unique_permutation(self,nums,curr_permutations, dictionary, permutations):
        if len(curr_permutations) == len(nums) and curr_permutations not in permutations:
            permutations.append(curr_permutations[:])
            return
        for num in nums:
            if dictionary[num]:
                dictionary[num] -= 1
                curr_permutations.append(num)
                self.find_unique_permutation(nums,curr_permutations, dictionary,permutations)
                dictionary[num] += 1
                curr_permutations.pop()
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        dictionary = Counter(nums)
        permutations = []
        self.find_unique_permutation(nums,[],dictionary,permutations)
        return permutations

s = Solution()
s.permuteUnique([1,-1,1,2,-1,2,2,-1])