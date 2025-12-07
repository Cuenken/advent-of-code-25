
import pandas as pd

def read_input():
    lines = pd.read_csv(
        './input.txt',
        sep=r'\s+',
        header=None
    )
    return lines.iloc[:-1].astype(int), lines.iloc[-1]

def solve():
    numbers, operations = read_input()
    result = 0
    for idx, column in enumerate(numbers.columns):
        operation = operations[idx]
        match operation:
            case '+': result += numbers[column].sum()
            case '*': result += numbers[column].prod()
    return result

if __name__ == '__main__':
    print(solve())