class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sorting the intervals
        intervals.sort(key=lambda x : x[0])

        rooms = [] # initializing a heap

        for i in intervals:
            if rooms and rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
        return len(rooms)






            

 

        