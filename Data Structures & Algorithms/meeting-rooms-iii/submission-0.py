from heapq import heapify,heappush as hpush, heappop as hpop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = [x for x in range(n)] 
        heapify(free)
        used = [] # stores the used rooms and wehn available like => (end,room_num)
        room_cnt = [0]*n
        meetings.sort()
        for start,end in meetings:

            while used and used[0][0] <= start:
                avail_time,room_num = hpop(used)
                hpush(free,room_num)
            
            # if free bcoz meeting starts on intended time 
            if free:
                room_num = hpop(free)
                hpush(used,(end,room_num))
            else:
            # no rooms free once anything becomes free we nee dto delay the time 
                avail_time,room_num = hpop(used)
                new_end = avail_time + (end-start)
                hpush(used,(new_end,room_num))
            
            room_cnt[room_num]+=1
        
        return room_cnt.index(max(room_cnt))

        