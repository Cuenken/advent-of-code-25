from typing import Final

JOLTAGE_DIGITS: Final[int] = 12

def read_input() -> list[str]:
    with open('./input.txt', 'r') as file:
        return [line.strip() for line in file]

def maximize_joltage(bank: list[str]):
    joltage = ""
    start_sequence_idx = 0
    for idx, i in enumerate(range(1, JOLTAGE_DIGITS + 1)):

        # Shortening of the end sequence as the loop advances
        end_sequence_idx = -JOLTAGE_DIGITS + idx + 1
        if end_sequence_idx == 0:
            end_sequence_idx = None

        # The available numbers get shorter as the loop advances
        available_numbers = bank[start_sequence_idx:end_sequence_idx]
        max_value = max(map(int, available_numbers))
        start_sequence_idx += available_numbers.index(str(max_value)) + 1
        joltage += str(max_value)

    return int(joltage)


def solve():
    banks = read_input()
    joltage = 0
    for bank in banks:
        joltage += maximize_joltage(list(bank))
    return joltage

if __name__ == '__main__':
    print(solve())