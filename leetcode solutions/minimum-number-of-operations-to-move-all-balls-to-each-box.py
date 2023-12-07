class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        total_moves = []
        for i in range(len(boxes)):
            curr = 0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=="1":
                    curr += abs(i-j)
            total_moves.append(curr)
        return total_moves