"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def find(id:int):
            for employee in employees:
                if employee.id == id:
                    return employee
        
        init = find(id)
        q = [init]
        visited = set()
        visited.add(id)

        ans = 0

        while q:
            curr = q.pop()
            ans += curr.importance

            for subs in curr.subordinates:
                if subs not in visited:
                    emp = find(subs)
                    q.append(emp)
        
        return ans