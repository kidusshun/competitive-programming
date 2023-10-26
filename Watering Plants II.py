class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i,j = 0, len(plants) - 1
        refills = 0
        a = capacityA
        b = capacityB

        while i<=j:
            if i == j:
                if b> a:
                    if b<plants[j]:
                        b = capacityB
                        refills +=1
                    b-=plants[j]
                else:
                    if a< plants[i]: 
                        a = capacityA
                        refills +=1
                    a-=plants[i]
            else:
                if a< plants[i]: 
                    a = capacityA
                    refills +=1
                a-=plants[i]

                if b< plants[j]: 
                    b = capacityB
                    refills +=1
                b-=plants[j]
            i+=1
            j-=1
        return refills