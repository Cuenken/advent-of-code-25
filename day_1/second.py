from day_1.first import Dial, read_input


def solve(marked_number: int = 0):
    dial = Dial(
        numbers=list(range(100)),
        starting_position=50
    )
    number_count = 0
    combination = read_input()
    for direction, steps in combination:
        for _ in range(steps):
            if direction == 'R':
                dial.right()
            else:
                dial.left()
            if dial.position == marked_number:
                number_count += 1
    return number_count


if __name__ == '__main__':
    print(solve())