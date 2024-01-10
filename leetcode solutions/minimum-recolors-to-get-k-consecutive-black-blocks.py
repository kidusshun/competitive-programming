class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        sub = blocks[:k]
        w_count = sub.count('W')
        min_ops = w_count
        i = 0
        for j in range(k,len(blocks)):
            if blocks[i] == 'W':
                w_count -=1
            if blocks[j] == 'W':
                w_count += 1
            i+=1
            min_ops = min(min_ops, w_count)
        return min_ops