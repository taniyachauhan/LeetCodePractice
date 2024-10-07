class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]==0:
            return True
        last = len(arr)-1
        queue = collections.deque()
        queue.append(start)
        visited = set()
        visited.add(start)


        while queue:
            stair = queue.popleft()


            backstep = stair - arr[stair]
            if 0 <= backstep and backstep not in visited:
                if arr[backstep] == 0:
                    return True
                queue.append(backstep)
                visited.add(backstep)


            frontstep = stair + arr[stair]
            if frontstep <= last and frontstep not in visited:
                if arr[frontstep] == 0:
                    return True
                queue.append(frontstep)
                visited.add(frontstep)
        return False
            



        