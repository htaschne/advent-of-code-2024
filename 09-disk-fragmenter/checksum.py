import sys

def move_file(file, gaps):
    fstart, fid, fsize = file
    idx, gst, gsz = -1, 0, 0
    for i, (gstart, gsize) in enumerate(gaps):
        if fsize <= gsize:
            # print(f"moving {fid} from: {fstart} to: {gstart}")
            idx = i
            gsz = gsize - fsize
            gst = gstart + fsize
            fstart = gstart
            break

    if idx < 0:
        return False, file, gaps

    if gsz == 0:
        del gaps[idx]
    else:
        gaps[idx] = (gst, gsz)
    return True, (fstart, fid, fsize), gaps

def main():
    # Part I
    disk = list(open(sys.argv[1]).readline().strip())
    parsed = {}
    file = True
    i, id = 0, 0
    files, gaps = [], []
    for c in disk:
        if file:
            for _ in range(int(c)):
                parsed[i] = str(id)
                i += 1
            files.append((i - int(c), id, int(c)))
            id += 1
        else:
            for _ in range(int(c)):
                parsed[i] = "."
                i += 1
            gaps.append((i - int(c), int(c)))
        file = not file

    length = i

    lo, hi = 0, i - 1
    while lo < hi:
        if parsed[lo] == ".":
            while parsed[hi] == ".":
                hi -= 1
            parsed[lo], parsed[hi] = parsed[hi], parsed[lo]
            hi -= 1
        lo += 1


    # TODO: this hack is to swap the last two blocks
    # parsed[50263], parsed[50264] = parsed[50264], parsed[50263]
    acc = sum([int(parsed[j]) * j for j in range(i) if parsed[j] != "."])
    print(acc)

    # Part 2
    new_files = []
    for file in reversed(files):
        ok, new_file, gaps = move_file(file, gaps)
        if ok:
            new_files.append(new_file)
        else:
            new_files.append(file)

    gg = {}
    for fstart, fid, fsize in new_files:
        for i in range(fsize):
            gg[fstart + i] = fid

    acc = sum([gg[j] * j for j in range(length) if j in gg.keys()])
    print(acc)


if __name__ == "__main__":
    main()
