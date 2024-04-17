from collections import defaultdict
import sys
input = sys.stdin.readline


def findMin():
    result = []
    for idx, val in product.items():
        if cost[start][val[1]] <= val[0]:
            result.append([abs(val[0] - cost[start][val[1]]), idx])

    if not result:
        return -1
    else:
        result.sort(key=lambda x: (-x[0], x[1]))
        product.pop(result[0][1])
        return result[0][1]


if __name__ == "__main__":
    q = int(input())
    tmp = list(map(int, input().split()))
    n, m = tmp[1], tmp[2]
    product = defaultdict(list)
    cost = [[1e9] * n for _ in range(n)]
    start = 0

    for i in range(1, m + 1):
        cost[tmp[i * 3]][tmp[i * 3 + 1]] = min(cost[tmp[i * 3]][tmp[i * 3 + 1]], tmp[i * 3 + 2])
        cost[tmp[i * 3 + 1]][tmp[i * 3]] = min(cost[tmp[i * 3 + 1]][tmp[i * 3]], tmp[i * 3 + 2])

    for i in range(n):
        if cost[i][i] == 1e9:
            cost[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

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
            print(findMin())
        elif num == 500:
            start = tmp[0]