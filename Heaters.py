class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        if len(heaters) == 1:
            target = heaters[0]

            l,r = 0,len(houses) - 1

            while l <= r:
                mid = (l+r)//2
                if houses[mid] > target:
                    l = mid + 1
                elif houses[mid] < target:
                    r = mid - 1
                else:
                    return houses[mid] - houses[0]
            return max((heaters[-1] - mid), (mid - heaters[0]))
        else:
            return 0

s = Solution()
s.findRadius([1,2,3], [2])