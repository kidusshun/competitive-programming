class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        return sum(salary[1:])/len(salary[1:])