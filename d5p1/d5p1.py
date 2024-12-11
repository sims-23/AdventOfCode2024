# cleaned up my previous code using claude
# defaultdict chosen since we want a default value of an array

from collections import defaultdict
from typing import List, Set, Dict
import pathlib

def parse_rules(line: str) -> tuple[int, int]:
    """Extract page numbers from a rule line containing '|'.
    Returns (before_page, after_page) tuple."""
    before_page, after_page = map(int, line.split("|"))
    return after_page, before_page

def parse_update(line: str) -> List[int]:
    """Convert a comma-separated line of numbers into a list of integers."""
    return list(map(int, line.strip().split(",")))

def process_update(update: List[int], page_rules: Dict[int, List[int]]) -> int:
    """
    Calculate the middle value of an update if its page order is valid.
    Returns 0 if any page appears before its dependencies.
    """
    comes_before: Set[int] = set()
    
    for page_num in update:
        if page_num in comes_before:
            return 0
        comes_before.update(page_rules[page_num])
    
    return update[len(update) // 2]

def calculate_page_updates(filepath: str) -> int:
    """
    Process a file containing page rules and updates.
    Returns the sum of valid middle values from updates.
    """
    page_rules = defaultdict(list)
    updates = []

    with open(filepath, "rt") as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            
            if '|' in line:
                after_page, before_page = parse_rules(line)
                page_rules[after_page].append(before_page)
            else:
                updates.append(parse_update(line))
    
    return sum(process_update(update, page_rules) for update in updates)

if __name__ == "__main__":
    filepath = pathlib.Path("./d5p1/input.txt")
    total = calculate_page_updates(filepath)
    print(total)