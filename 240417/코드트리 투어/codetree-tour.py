from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def findMin():
    result = []
    for idx, val in product.items():
        if cost[start][val[1]] <= val[0]:
            result.append([val[0] - cost[start][val[1]], idx])

    if not result:
        return -1
    else:
        result.sort(key=lambda x: (-x[0], x[1]))
        product.pop(result[0][1])
        return result[0][1]


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
    cost[start] = dist

if __name__ == "__main__":
    q = int(input())
    tmp = list(map(int, input().split()))
    n, m = tmp[1], tmp[2]
    product = defaultdict(list)
    graph = [[] for _ in range(n)]
    cost = [[1e9] * n for _ in range(n)]
    start = 0

    for i in range(1, m + 1):
        if tmp[i * 3] != tmp[i * 3 + 1]:
            graph[tmp[i * 3]].append((tmp[i * 3 + 1], tmp[i * 3 + 2]))
            graph[tmp[i * 3 + 1]].append((tmp[i * 3], tmp[i * 3 + 2]))

    for i in range(q - 1):
        num, *tmp = list(map(int, input().split()))
        if num == 200:
            product[tmp[0]] = [tmp[1], tmp[2]]
        elif num == 300:
            if product[tmp[0]] != list():
                product.pop(tmp[0])
            else:
                product.pop(tmp[0])
        elif num == 400:
            dijkstra()
            print(findMin())
        elif num == 500:
            start = tmp[0]