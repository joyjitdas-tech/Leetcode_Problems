import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l =1
        r = max(piles)


        while l <= r:
            speed = l +(r-l)//2
            
            sum = 0
            for num in piles:
                x = math.ceil(num/speed)
                sum += x
            if sum > h:
                l = speed +1
            else:
                r = speed-1

        return l

