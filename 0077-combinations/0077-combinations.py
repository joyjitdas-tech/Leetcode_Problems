class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def back(start,current):
            if len(current) == k:
                result.append(current.copy())
                return
            
            for i in range(start,n+1):
                current.append(i)

                back(i+1,current)
                current.pop()
                

        back(1,[])
        
        return result
