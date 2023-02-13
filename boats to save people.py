class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right=0,len(people)-1
        num_boats=0
        while left<=right:
            if (people[left]+people[right]) <= limit:
                num_boats+=1
                left+=1
                right-=1
            else:
                num_boats+=1
                right-=1
        return num_boats