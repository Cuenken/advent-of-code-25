
def read_input():
    with open('input.txt') as f:
        fresh_ids = list()
        available_ids = list()
        switch = False
        for line in f.readlines():
            if line == '\n':
                switch = True
                continue
            if not switch:
                start, end = line.strip().split('-')
                fresh_ids.append([start, end])
            else:
                available_ids.append(line.strip())
        return fresh_ids, available_ids

def solve():
    fresh_ids, available_ids = read_input()
    fresh_available_ids = 0
    for available_id in available_ids:
        for start, end in fresh_ids:
            if int(start) <= int(available_id) <= int(end):
                fresh_available_ids += 1
                break
    return fresh_available_ids

if __name__ == '__main__':
    print(solve())