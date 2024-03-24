import heapq
def minMeetingRooms(meetings):
    if not meetings:
        return 0
    if not meetings[0]:
        return 1
    meetings = sorted(meetings, key=lambda x:x[1])
    print(meetings)
    #[[5, 10], [15, 20], [0, 30]]
    queue = []
    heapq.heappush(queue, meetings[0][1])
    for i in range(1, len(meetings)):
        if meetings[i][0] > queue[0]:
            heapq.heappop(queue)
        heapq.heappush(queue, meetings[i][1])
    return len(queue)

nums=[[0,30], [5,10], [15,20]]
# nums=[[0,30]]


a = minMeetingRooms(nums)
print(a)