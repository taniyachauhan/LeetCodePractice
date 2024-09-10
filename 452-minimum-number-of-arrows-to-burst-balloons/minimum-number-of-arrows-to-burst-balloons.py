class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort()
        # print(points)
        # stack = []

        # i = 0
        # j = 1

        # while i < len(points):
        #     while j < len(points) and points[j][0] <= points[i][1]:
        #         j += 1
        #     stack.append([points[i][0], points[j-1][1]])
            
        #     i = j
        #     j = i + 1


        # SECOND ATTEMPT USING sorting and stack or heap

        points.sort(key = lambda x:x[1])
        print(points)
        count = 0
        i = 0
        while i < len(points):
            j = i+1
            while j < len(points) and points[j][0] <= points[i][1]:
                j += 1
            count += 1

            i = j
        print(count)
        return count
            


        # return len(stack)
   


        