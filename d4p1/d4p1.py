import numpy as np
    
directions = [(-1, -1), (0, -1), (1, -1),  # up-left, up, up-right
                (1, 0),                      # right
                (1, 1), (0, 1), (-1, 1),     # down-right, down, down-left
                (-1, 0)]                     # left

def inbounds(x,y, rows, cols):
    return x>=0 and x<rows and y>=0 and y<cols

def check_direction(x, y, dx, dy, rows, cols):
    for i, char in enumerate(['M', 'A', 'S']):
        next_x = x + dx * (i + 1)
        next_y = y + dy * (i + 1)
        if not inbounds(next_x, next_y, rows, cols) or data[next_x][next_y] != char:
            return False
    return True

def find_xmas(data):
    count = 0
    rows, cols = data.shape

    for x in range(rows):
        for y in range(cols):
            if data[x][y] == 'X': 
                for dx, dy in directions:
                    if check_direction(x,y,dx,dy, rows, cols):
                        count += 1
    
    return count

data = np.genfromtxt('./d4p1/input.txt', dtype=str, delimiter=1)
print(find_xmas(data))



