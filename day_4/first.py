from __future__ import annotations
from typing import TypedDict

class PaperRollMatrix(TypedDict):
    top_left: PaperRoll | None
    top_middle: PaperRoll | None
    top_right: PaperRoll | None
    left_side: PaperRoll | None
    right_side: PaperRoll | None
    bottom_left: PaperRoll | None
    bottom_middle: PaperRoll | None
    bottom_right: PaperRoll | None

class PaperRoll:
    def __init__(self, adjacent_items: PaperRollMatrix):
        self.adjacent_items = adjacent_items

    @property
    def neighbors(self) -> int:
        return sum(1 for v in self.adjacent_items.values() if v is not None)

    def __repr__(self):
        return "@"


class Shelve:
    def __init__(self, items: str, upper_shelve: "Shelve | None" = None, lower_shelve: "Shelve | None" = None, paper_icon: str = '@'):
        self._raw_items = list(items)
        self.upper_shelve = upper_shelve
        self.lower_shelve = lower_shelve
        self._paper_icon = paper_icon
        self._items: list[PaperRoll | None] | None = None

    @property
    def items(self) -> list[PaperRoll | None]:
        if self._items is not None:
            return self._items

        items: list[PaperRoll | None] = []
        previous_item: PaperRoll | None = None

        for idx, spot in enumerate(self._raw_items):
            if spot == self._paper_icon:
                matrix: PaperRollMatrix = {
                    "top_left": None,
                    "top_middle": None,
                    "top_right": None,
                    "left_side": previous_item,
                    "right_side": None,
                    "bottom_left": None,
                    "bottom_middle": None,
                    "bottom_right": None,
                }
                item = PaperRoll(adjacent_items=matrix)

                if previous_item:
                    previous_item.adjacent_items["right_side"] = item
            else:
                item = None

            previous_item = item
            items.append(item)

        self._items = items
        return items

    def remove_item(self, position: int) -> PaperRoll | None:
        items = self.items
        items[position]= None

    def __repr__(self):
        shelve = ""
        for item in self.items:
            shelve += str(item) if item else "."
        return shelve

def link_neighbors(grid: list[Shelve]) -> None:
    for row_idx, shelve in enumerate(grid):
        row_items = shelve.items

        for col_idx, roll in enumerate(row_items):
            if roll is None:
                continue

            roll.adjacent_items["left_side"] = row_items[col_idx - 1] if col_idx > 0 else None
            roll.adjacent_items["right_side"] = (
                row_items[col_idx + 1] if col_idx + 1 < len(row_items) else None
            )

            if row_idx > 0:
                upper_items = grid[row_idx - 1].items
                roll.adjacent_items["top_left"] = upper_items[col_idx - 1] if col_idx > 0 else None
                roll.adjacent_items["top_middle"] = upper_items[col_idx]
                roll.adjacent_items["top_right"] = (
                    upper_items[col_idx + 1] if col_idx + 1 < len(upper_items) else None
                )
            else:
                roll.adjacent_items["top_left"] = None
                roll.adjacent_items["top_middle"] = None
                roll.adjacent_items["top_right"] = None

            if row_idx + 1 < len(grid):
                lower_items = grid[row_idx + 1].items
                roll.adjacent_items["bottom_left"] = lower_items[col_idx - 1] if col_idx > 0 else None
                roll.adjacent_items["bottom_middle"] = lower_items[col_idx]
                roll.adjacent_items["bottom_right"] = (
                    lower_items[col_idx + 1] if col_idx + 1 < len(lower_items) else None
                )
            else:
                roll.adjacent_items["bottom_left"] = None
                roll.adjacent_items["bottom_middle"] = None
                roll.adjacent_items["bottom_right"] = None

def load_shelves() -> list[Shelve]:
    with open('./input.txt', 'r') as file:
        grid = []
        previous_shelve = None
        for idx, line in enumerate(file):
            current_shelve = Shelve(
                line.strip(),
                upper_shelve=previous_shelve
            )
            if previous_shelve:
                previous_shelve.lower_shelve = current_shelve
            previous_shelve = current_shelve
            grid.append(previous_shelve)
        return grid


def solve():
    grid = load_shelves()
    link_neighbors(grid)
    accesible_paper_rolls = 0
    for shelve in grid:
        for paper_roll in shelve.items:
            if paper_roll and paper_roll.neighbors < 4:
                accesible_paper_rolls += 1
    return accesible_paper_rolls

if __name__ == '__main__':
    print(solve())
