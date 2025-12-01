
class Dial:
    def __init__(self, numbers: list[int], starting_position: int = 50):
        if starting_position not in numbers:
            raise ValueError(f"{starting_position} is not in the dial")
        self.numbers = numbers
        self.starting_position = starting_position
        self.position = starting_position

    def right(self):
        if self.position == len(self.numbers) - 1:
            self.position = self.numbers[0]
        else:
            self.position += 1

    def left(self):
        if self.position == self.numbers[0]:
            self.position = len(self.numbers) - 1
        else:
            self.position -= 1

def read_input() -> list[tuple[str, int]]:
    with open('./input.txt', 'r') as file:
        return [(line.strip()[0], int(line.strip()[1:])) for line in file]


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