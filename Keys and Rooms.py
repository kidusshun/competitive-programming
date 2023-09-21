class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set([0])

        while q:
            curr = q.popleft()
            for neigh in rooms[curr]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
        
        if len(visited) == len(rooms): return True
        return False