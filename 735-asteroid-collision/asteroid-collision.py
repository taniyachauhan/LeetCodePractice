class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = []
        
        # for asteroid in asteroids:
        #     while stack and asteroid < 0 and stack[-1] > 0:
        #         top = stack.pop()
        #         if abs(top) == abs(asteroid):
        #             break
        #         elif abs(top) > abs(asteroid):
        #             stack.append(top)
        #             break
        #     else:
        #         stack.append(asteroid)
        
        # return stack

        # SECOND ATTEMPT

        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) < abs(stack[-1]):
                    break
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    break
                elif abs(asteroid) > abs(stack[-1]):
                        stack.pop()     
            else:
                stack.append(asteroid)
        return stack






                 