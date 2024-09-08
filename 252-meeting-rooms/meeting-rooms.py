class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        # Sorting the intervals
        intervals.sort(key=lambda x : x[0])

        rooms = [] # initializing a heap

        for i in intervals:
            if rooms and rooms[0] <= i[0]:
                heapq.heappop(rooms)
                
            heapq.heappush(rooms, i[1])
        if len(rooms)==1:
            return True
        return False
