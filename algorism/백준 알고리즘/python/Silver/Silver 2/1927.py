import heapq

N = int(input())

heap = []

for i in range(N):
    n = int(input())

    if n != 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0: #len가 정수이면
            print(0)
        else:
            heapq.heappop(heap)