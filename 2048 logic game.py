import random
n = 4

def start_game():
    mat = []
    for _ in range(n):
        mat.append([0]*n)
    return mat

def add_new_2(mat):
    
    r = random.randint(0,n-1)
    c = random.randint(0,n-1)
    while(mat[r][c] != 0):
        r = random.randint(0,n-1)
        c = random.randint(0,n-1)
    mat[r][c] = 2

def reverse(mat):
    new_mat = []
    for i in range(n):
        new_mat.append([])
        for j in range(n):
            new_mat[i].append(mat[i][n-j-1])
    
    return new_mat

def transpose(mat):
    
    new_mat = []
    for i in range(n):
        new_mat.append([])
        for j in range(n):
            new_mat[i].append(mat[j][i])
    return new_mat

def merge(mat):
    changed = False
    for i in range(n):
        for j in range(n-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
                changed = True
    return mat,changed
           
def compress(mat):
    
    changed = False
    new_mat = []
    for i in range(n):
        new_mat.append([0]*n)
    
    for i in range(n):
        pos = 0
        for j in range(n):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j!= pos:
                    changed = True
                pos+=1
    return new_mat,changed

def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed

def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed

def move_right(grid):
    
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

def move_left(grid):
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid, _ = compress(new_grid)
    return new_grid,changed
  
def get_current_state(mat):
    # Anywhere 2048 is present
    for i in range(n):
        for j in range(n):
            if (mat[i][j] == 2048):
                return 'WON'
    #Anywhere 0 is present
    for i in range(n):
        for j in range(n):
            if(mat[i][j] == 0):
                return 'GAME NOT OVER'
    # Every Row and Column except last row and last column
    for i in range(n-1):
        for j in range(n-1):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return 'GAME NOT OVER'
    #Last Row
    for j in range(n-1):
        if mat[n-1][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    #Last Column
    
    for i in range(n-1):
        if mat[i][n-1] == mat[i+1][3]:
            return 'GAME NOT OVER'
        
    return 'LOST'

def print_grid(mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=' ')
        print()

###########

mat = start_game()
add_new_2(mat)
print_grid(mat)
change = False

while True:
    key = input()
    if key == "w":
        mat, change = move_up(mat)

    if key == "a":
        mat, change = move_left(mat)

    if key == "s":
        mat, change = move_down(mat)

    if key == "d":
        mat, change = move_right(mat)

    result = get_current_state(mat)
    if result == 'WON':
        print_grid(mat)
        print('YOU WON :) !!!')
        break

    if result == 'LOST':
        print_grid(mat)
        print('YOU LOST :(')
        break

    if change:
        add_new_2(mat)
        change = False
    print_grid(mat)