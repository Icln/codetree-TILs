from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

def renew():
    for key, val in product.items():
        product[key] = [(val[1] - cost[val[2]]) * -1, val[1], val[2]]
        heapq.heappush(result, [(val[1] - cost[val[2]]) * -1, key])


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
    product = defaultdict(list)
    graph = [[] for _ in range(n)]
    start = 0

    for i in range(1, m + 1):
        if tmp[i * 3] != tmp[i * 3 + 1]:
            graph[tmp[i * 3]].append((tmp[i * 3 + 1], tmp[i * 3 + 2]))
            graph[tmp[i * 3 + 1]].append((tmp[i * 3], tmp[i * 3 + 2]))

    cost = dijkstra()
    result = []
    for i in range(q - 1):
        num, *tmp = list(map(int, input().split()))
        if num == 200:
            product[tmp[0]] = [(tmp[1] - cost[tmp[2]]) * -1, tmp[1], tmp[2]]
            heapq.heappush(result, [(tmp[1] - cost[tmp[2]]) * -1, tmp[0]])

        elif num == 300:
            if product[tmp[0]] != list():
                result.remove([product[tmp[0]][0], tmp[0]])
                product.pop(tmp[0])
            else:
                product.pop(tmp[0])

        elif num == 400:
            if not result:
                print(-1)
            else:
                if result[0][0] > 0:
                    print(-1)
                else:
                    node = heapq.heappop(result)
                    print(node[1])
                    product.pop(node[1])

        elif num == 500:
            start = tmp[0]
            cost = dijkstra()
            result = []
            renew()