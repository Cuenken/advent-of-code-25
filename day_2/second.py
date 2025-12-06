
def read_input() -> str:
    with open('./input.txt', 'r') as file:
        return file.read()

def get_intervals(string: str) -> list[str]:
    return string.split(',')

def get_invalid_ids_from_interval(interval: list[int]) -> list[int]:
    invalid_ids = []
    for number in interval:

        possible_segments = get_possible_segments(number_length := len(number_str := str(number)))

        # Test of each segment case
        for segment in possible_segments:
            previous_segment = None
            ko = None
            for i in range(0, number_length, segment):
                if previous_segment is None:  # first iteration
                    previous_segment = number_str[i: i+segment]
                if number_str[i: i+segment] != previous_segment: # not equal!
                    ko = True
                    break
                previous_segment = number_str[i: i+segment]
            if not ko:
                invalid_ids.append(number)
                break

    return invalid_ids

def get_possible_segments(number_length: int) -> list[int]:
    segments = []
    for i in range(1, number_length // 2 + 1):
        if number_length % i:
            continue
        segments.append(i)  # add only divisible numbers
    return segments


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