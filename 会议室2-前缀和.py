
def minMeetingRooms(meetings):
    if not meetings:
        return 0
    if not meetings[0]:
        return 1
    meetings = sorted(meetings, key=lambda x:x[1])
    print(meetings)
    #[[5, 10], [15, 20], [0, 30]]
    trie = [0 for _ in range(meetings[-1][1] + 1)]
    # 31个0
    print(trie)

    for m in meetings:
        begin, end = m[0], m[1]
        trie[begin] += 1
        trie[end] -= 1

    for i, val in enumerate(trie):
        if i>0:
            trie[i] += trie[i-1]
    return max(trie)

nums=[[0,30], [5,10], [15,20]]
# nums=[[0,30]]

a = minMeetingRooms(nums)
print(a)