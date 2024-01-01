class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        print(tasks)
        ans = 0
        for i in range(0,len(tasks),4):
            curr = max(tasks[i:i+4])
            ans = max(curr+processorTime[i//4], ans)
        return ans