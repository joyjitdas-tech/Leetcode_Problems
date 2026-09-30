class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = []
        for i in range(len(speed)):
            pair.append((position[i],speed[i]))
        
        pair.sort(reverse=True)

        stack = []
        
        for pos,spd in pair:
            time = (target-pos)/spd
            

            if not stack or time > stack[-1]:
                stack.append(time)
                
        return len(stack)