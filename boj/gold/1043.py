# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# t = list(map(int, input().split()))
# trueman = set(t[1:])
#
# parties = []
# for _ in range(m):
#     data = list(map(int,input().split()))
#     party_members = set(data[1:])
#     parties.append(party_members)
#
#
# for _ in range(m):
#     for party in parties:
#         if party & trueman:
#             trueman.update(party)
#
# lie = 0
# for party in parties:
#     if not (party & trueman):
#         lie += 1
# print(lie)

import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


n, m = map(int, input().split())
truth_input = list(map(int, input().split()))
truth_people = truth_input[1:]

parent = [i for i in range(n + 1)]

parties = []
for _ in range(m):
    p_data = list(map(int, input().split()))
    p_len = p_data[0]
    p_members = p_data[1:]
    parties.append(p_members)

    for i in range(len(p_members) - 1):
        union(p_members[i], p_members[i+1])

truth_roots = set()
for person in truth_people:
    truth_roots.add(find(person))

ans = 0
for party in parties:
    root = find(party[0])
    if root not in truth_roots:
        ans += 1

print(ans)