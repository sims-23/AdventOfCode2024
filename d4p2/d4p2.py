import numpy as np

# noticed that around the a, the sequence mmss cycles along the positions in order to be valid
# so taking those values and seeing if it's one of the "cycled" sequence, then it makaes a valid x-mas

def inbounds(x,y, m, n):
    return x>=0 and x<m and y>=0 and y<n

def check_ms_sequence(data, x, y, m, n):
    pos1 = (x-1, y-1)  
    pos2 = (x+1, y-1)  
    pos3 = (x+1, y+1)  
    pos4 = (x-1, y+1)  
    
    positions = [pos1, pos2, pos3, pos4]
    for px, py in positions:
        if not inbounds(px, py, m, n):
            return False
            
    sequence = (data[pos1[0]][pos1[1]] + 
               data[pos2[0]][pos2[1]] +
               data[pos3[0]][pos3[1]] +
               data[pos4[0]][pos4[1]])
            
    # Check if it matches any valid pattern
    valid_sequences = ['MMSS', 'MSSM', 'SSMM', 'SMMS']
    return sequence in valid_sequences

def find_x_mas(data):
    count = 0
    m, n = data.shape

    for x in range(m):
        for y in range(n):
            if data[x][y] == 'A':
                if check_ms_sequence(data, x, y, m, n):
                    count += 1
    return count

data = np.genfromtxt('./d4p2/input.txt', dtype=str, delimiter=1)
print(find_x_mas(data))




