
def read_input() -> str:
    with open('./input.txt', 'r') as file:
        return file.read()

def get_intervals(string: str) -> list[str]:
    return string.split(',')

def get_invalid_ids_from_interval(interval: list[int]) -> list[int]:
    invalid_ids = []
    for number in interval:
        # discard odd numbers since they can't have two equal segments
        if (number_length := len(str_number := str(number))) % 2:
            continue
        # determine segment length and compare
        segment_length = int(number_length / 2)
        if str_number[:segment_length] == str_number[segment_length:]:
            invalid_ids.append(number)
    return invalid_ids

def solve():
    solution = 0
    for i in get_intervals(read_input()):
        start = int(i.split('-')[0])
        end = int(i.split('-')[1])
        interval = list(range(start, end + 1))
        invalid_ids = get_invalid_ids_from_interval(interval)
        solution +=  sum(invalid_ids)
    return solution

if __name__ == '__main__':
    print(solve())