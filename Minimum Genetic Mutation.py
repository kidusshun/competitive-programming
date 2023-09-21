class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        def is_valid_mutation(gene1, gene2):
            diff_count = 0
            for i in range(len(gene1)):
                if gene1[i] != gene2[i]:
                    diff_count += 1
                    if diff_count > 1:
                        return False
            return diff_count == 1
            
        visited = set()
        queue = deque([(startGene, 0)])

        while queue:
            gene, mutations = queue.popleft()
            if gene == endGene:
                return mutations
            visited.add(gene)
            
            for neighbor in bank:
                if neighbor not in visited and is_valid_mutation(gene, neighbor):
                    queue.append((neighbor, mutations + 1))
        
        return -1