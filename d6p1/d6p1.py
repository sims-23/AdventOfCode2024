from typing import List, Set, Tuple
import pathlib

def out_of_bounds(pos: Tuple[int, int], height: int, width: int) -> bool:
    """Check if position is out of bounds"""
    row, col = pos
    return row < 0 or col < 0 or row >= height or col >= width

def change_dir(dir: str) -> str:
    """Turn right 90 degrees"""
    directions = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up"
    }
    return directions[dir]

def get_next_pos(dir: str, pos: Tuple[int, int]) -> Tuple[int, int]:
    """Get next position in current direction"""
    row, col = pos
    match dir:
        case "up":
            return (row - 1, col)
        case "right":
            return (row, col + 1)
        case "down":
            return (row + 1, col)
        case "left":
            return (row, col - 1)
    return pos

def load_and_find(path: str) -> Tuple[List[List[str]], Tuple[int, int]]:
    """Load the lab layout and find starting position"""
    lab = []
    start_pos = None

    with open(path) as file:
        for row_idx, line in enumerate(file):
            row = list(line.rstrip('\n'))
            lab.append(row)
            if "^" in row:
                col_idx = row.index("^")
                start_pos = (row_idx, col_idx)
    
    return lab, start_pos

def calculate_distinct_positions(path: str) -> int:
    """Calculate number of distinct positions visited by guard before leaving map"""
    lab, start_pos = load_and_find(path)
    if not start_pos:
        return 0

    height = len(lab)
    width = len(lab[0])
    
    dir = "up"
    pos = start_pos
    visited = {pos}  # Using set for distinct positions

    while True:
        next_pos = get_next_pos(dir, pos)
        
        # Exit if next move would be out of bounds
        if out_of_bounds(next_pos, height, width):
            break
            
        # Now safe to check this position in the grid
        if lab[next_pos[0]][next_pos[1]] == "#":
            dir = change_dir(dir)
        else:
            pos = next_pos
            visited.add(pos)
    
    return len(visited)

if __name__ == "__main__":
    filepath = pathlib.Path("d6p1") / "input.txt"
    total = calculate_distinct_positions(str(filepath))
    print(total)