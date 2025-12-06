
import numpy as np

def read_input() -> list[str]:
    with open('./input.txt', 'r') as file:
        return [line.strip() for line in file]

def maximize_joltage(bank: list[str]):
    v = np.array(bank, dtype=object)
    joltage_matrix = v[:, None] + v[None, :]
    accepted_values = np.triu(joltage_matrix, k=1)
    return accepted_values.astype(int).max()


def solve():
    banks = read_input()
    joltage = 0
    for bank in banks:
        joltage += maximize_joltage(list(bank))
    return joltage

if __name__ == '__main__':
    print(solve())