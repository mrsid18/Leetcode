class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cc = Counter(tasks)
        
        maxcnt = [-val for val in cc.values()]
        heapq.heapify(maxcnt)
        
        time = 0
        queue = deque([])
        
        while queue or maxcnt:
            time+=1
            
            if not maxcnt:
                time = queue[0][1]
            else:
                count = heapq.heappop(maxcnt)
                count += 1
                if count: queue.append((count, time+n))
            
            if queue and queue[0][1]==time:
                heapq.heappush(maxcnt, queue.popleft()[0])
            
        return time
        
        
        