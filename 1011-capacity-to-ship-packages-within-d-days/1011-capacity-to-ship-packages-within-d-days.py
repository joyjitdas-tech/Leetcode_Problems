class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            capacity = l+(r-l)//2

            day_need = 1
            w= 0

            for num in weights:
                if (w+num) > capacity:
                    day_need +=1
                    w = 0
                w += num

            if day_need > days:
                l = capacity+1
            else:
                r = capacity -1
        return l