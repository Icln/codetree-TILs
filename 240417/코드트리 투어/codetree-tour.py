from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def sell():
    while product:
        p = product[0]
        if p[0] > 0:
            break
        heapq.heappop(product)
        if not cancel[p[1]]:
            return p[1]
    return -1

def renew():
    arr = []
    while product:
        a = heapq.heappop(product)
        a = [(a[2] - cost[a[3]]) * -1, a[1], a[2], a[3]]
        heapq.heappush(arr, a)

    return arr

def dijkstra():
    q, dist = [], [1e9] * n
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        time, cur = heapq.heappop(q)
        if dist[cur] < time:
            continue
        for next in graph[cur]:
            if next[1] + time < dist[next[0]]:
                dist[next[0]] = next[1] + time
                heapq.heappush(q, (dist[next[0]], next[0]))

    return dist


if __name__ == "__main__":
    q = int(input())
    tmp = list(map(int, input().split()))
    n, m = tmp[1], tmp[2]
    graph = [[] for _ in range(n)]
    start = 0

    for i in range(1, m + 1):
        if tmp[i * 3] != tmp[i * 3 + 1]:
            graph[tmp[i * 3]].append((tmp[i * 3 + 1], tmp[i * 3 + 2]))
            graph[tmp[i * 3 + 1]].append((tmp[i * 3], tmp[i * 3 + 2]))

    cost = dijkstra()
    product = []
    made = [False] * 30005
    cancel = [False] * 30005

    for i in range(q - 1):
        num, *tmp = list(map(int, input().split()))
        if num == 200:
            made[tmp[0]] = True
            heapq.heappush(product, [(tmp[1] - cost[tmp[2]]) * -1, tmp[0], tmp[1], tmp[2]])
        elif num == 300:
            if made[tmp[0]]:
                cancel[tmp[0]] = True
        elif num == 400:
            print(sell())
        elif num == 500:
            start = tmp[0]
            cost = dijkstra()
            product = renew()