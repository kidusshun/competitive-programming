class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=[]
        for log in logs:
            if log == '../' and len(ans) > 0:
                ans.pop()
            elif log == '../':
                continue
            elif log == './':
                continue
            else:
                ans.append(log)
        return len(ans)