class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        deleted = 0

        for j in range(len(strs[0])):
            prev = strs[0][j]
            for i in range(1,len(strs)):
                curr = strs[i][j]
                if ord(prev) > ord(curr):
                    deleted += 1
                    break
                prev = curr
        return deleted