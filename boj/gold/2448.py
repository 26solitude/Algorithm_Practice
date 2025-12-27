import sys


def solve():
    n = int(sys.stdin.readline())

    star = ['  *  ', ' * * ', '*****']

    def make_stars(n):
        if n == 3:
            return star

        prev_stars = make_stars(n // 2)
        padding = ' ' * (n // 2)

        now_stars = []

        for line in prev_stars:
            now_stars.append(padding + line + padding)

        for line in prev_stars:
            now_stars.append(line + ' ' + line)

        return now_stars

    print('\n'.join(make_stars(n)))


solve()
