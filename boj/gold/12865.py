import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())

    items = [list(map(int, input().split())) for _ in range(n)]
    items.sort(key=lambda x: x[0], reverse=True)

    dp = {0: 0}

    for w, v in items:
        temp = {}

        for old_v, old_w in dp.items():
            new_v = old_v + v
            new_w = old_w + w

            if new_w > k:
                continue

            if new_w < dp.get(new_v, k + 1):
                temp[new_v] = new_w

        dp.update(temp)

    print(max(dp.keys()))


if __name__ == "__main__":
    solve()
