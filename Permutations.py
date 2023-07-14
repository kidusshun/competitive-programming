class Solution:
    def findAllPermutations(self,nums, curr_permutation, visited, permutations):
        if len(curr_permutation) == len(nums):
            permutations.append(curr_permutation[::])
            return
        for num in nums:
            if num in visited: continue
            visited.add(num)
            curr_permutation.append(num)
            self.findAllPermutations(nums, curr_permutation, visited, permutations)
            visited.remove(num)
            curr_permutation.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.findAllPermutations(nums,[], set(),permutations)
        return permutations
