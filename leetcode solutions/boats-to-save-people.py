class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0, len(people)-1
        min_boats = 0
        while left<=right:
            if left==right and people[left]<=limit:
                min_boats+=1
                break
            elif people[left]+people[right]<=limit:
                min_boats+=1
                left+=1
            else:
                min_boats+=1
            right-=1
        return min_boats