
import sys

def valid_range(r, c):
    global mr, mc
    return 0 <= r <= mr and 0 <= c <= mc

def valid_hike(r, c, nr, nc):
    global g
    return g[(r, c)] + 1 == g[(nr, nc)]


def paths(r, c):
    pt = []
    for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
        nr, nc = r + dr, c + dc
        if valid_range(nr, nc) and valid_hike(r, c, nr, nc):
            pt.append((r + dr, c + dc))
    return pt


def hike(r: int, c: int, seen: set[tuple[int, int]] = set()) -> int:
    global g
    if (r, c) not in seen:
        seen.add((r, c))

    if g[(r, c)] == 9:
        return 1

    acc = 0
    for nr, nc in paths(r, c):
        if not (nr, nc) in seen:
            acc += hike(nr, nc, seen)
    
    return acc


def main():
    global g, mr, mc

    starts = set()
    for r, line in enumerate(open(sys.argv[1]).readlines()):
        for c, col in enumerate(line.strip()):
            g[(r, c)] = int(col)
            mr, mc = max(r, mr), max(c, mc)
            if col == "0":
                starts.add((r, c))


    acc = sum([hike(r, c) for r, c in starts])
    print(acc)


g = {}
mr, mc = 0, 0
if __name__ == "__main__":
    main()
