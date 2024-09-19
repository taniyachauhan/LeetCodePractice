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


        stack =[]

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                top = stack.pop()
                if abs(asteroid) > top:
                    continue
                elif abs(asteroid) == top:
                    break
                else:
                    stack.append(top)
                    break  
            else:  
                stack.append (asteroid)
        return stack







                 