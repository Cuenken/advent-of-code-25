from day_5.first import read_input



def solve():
    fresh_ids, _ = read_input()
    fresh_ids = sorted(list(set((int(start), int(end)) for start, end in fresh_ids)) ) # remove duplicates
    merged = []
    for start, end in fresh_ids:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    fresh_ids_count = sum(end - start + 1 for start, end in merged)


    return fresh_ids_count

if __name__ == '__main__':
    print(solve())