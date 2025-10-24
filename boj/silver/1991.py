import sys

input = sys.stdin.readline

n = int(input())
tree = {}

for i in range(n):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]


def pre_dfs(node):
    if node == '.':
        return
    print(node, end='')
    pre_dfs(tree[node][0])
    pre_dfs(tree[node][1])


def in_dfs(node):
    if node == '.':
        return
    in_dfs(tree[node][0])
    print(node, end='')
    in_dfs(tree[node][1])


def post_dfs(node):
    if node == '.':
        return
    post_dfs(tree[node][0])
    post_dfs(tree[node][1])
    print(node, end='')


pre_dfs('A')
print()
in_dfs('A')
print()
post_dfs('A')
