class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans_count = Counter(answers)
        num_rabits = 0
        for key, value in ans_count.items():
            num_rabits += math.ceil(value/(key+1))* (key+1)
        return num_rabits