
from day_4.first import link_neighbors, load_shelves


def removal_iteration(grid):
    removed = 0
    for shelve in grid:
        for idx, paper_roll in enumerate(shelve.items):
            if paper_roll and paper_roll.neighbors < 4:
                shelve.remove_item(idx)
                removed += 1
    print(f"Removed items: {removed}")
    link_neighbors(grid)
    return removed

def solve():
    grid = load_shelves()
    link_neighbors(grid)
    first_iteration_removed_items = removal_iteration(grid)
    loop_removed_items = 1
    total_removed = first_iteration_removed_items
    while loop_removed_items > 0:
        loop_removed_items = removal_iteration(grid)
        total_removed += loop_removed_items
    return total_removed


if __name__ == '__main__':
    print(solve())
