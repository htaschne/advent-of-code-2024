
import sys

from collections import Counter

ranges = [list(map(int, line.strip().split("   "))) for line in open(sys.argv[1]).readlines()]

lo = [r[0] for r in ranges]
hi = [r[1] for r in ranges]

lo.sort()
hi.sort()

dists = [abs(l - h) for l, h in zip(lo, hi)]
acc = sum(dists)
print(acc)

c = Counter(lo)
acc = sum([x * c[x] for x in hi])
print(acc)