# write your code here
cells = raw_input("Enter cells: ")
square = []
new_square = []  # Only contains the X, O, _ no extra space or characters
print("---------")
for i in range(0, 9, 3):
    line = "| "
    new_line = []
    for j in range(3):
        line += cells[i+j] + " "
        new_line.append(cells[i+j])
    line += "|"
    square.append(line)
    new_square.append(new_line)

for line in square:
    print(line)
print("---------")



def check_win(win_O, win_X):
    if win_O == 3 and win_X == 3:
        return "Impossible"
    elif win_O == 3:
        return "O wins"
    elif win_X == 3:
        return "X wins"
    else:
        return "Nothing much"

def who_won():
    # Horizontal win
    num_O, num_X = 0, 0
    for i in range(3):
        for j in range(3):
            if new_square[i][j] == 'O':
                num_O += 1
            elif new_square[i][j] == 'X':
                num_X += 1
    if abs(num_O - num_X) > 1:
        return "Impossible"
        
    listwin_X = []
    listwin_O = []
    for i in range(3):
        win_O, win_X = 0, 0
        for j in range(3):
            if new_square[i][j] == 'O':
                win_O += 1
            elif new_square[i][j] == 'X':
                win_X += 1
        listwin_X.append(win_X)
        listwin_O.append(win_O)

    if 3 in listwin_X and 3 in listwin_O:
        return "Impossible"
    elif 3 in listwin_O:
        return "O wins"
    elif 3 in listwin_X:
        return "X wins"
    
    # Vertical win
    listwin_X = []
    listwin_O = []
    for j in range(3):
        win_O, win_X = 0, 0
        for i in range(3):
            if new_square[i][j] == 'O':
                win_O += 1
            elif new_square[i][j] == 'X':
                win_X += 1
        listwin_X.append(win_X)
        listwin_O.append(win_O)

    if 3 in listwin_X and 3 in listwin_O:
        return "Impossible"
    elif 3 in listwin_O:
        return "O wins"
    elif 3 in listwin_X:
        return "X wins"
    
    # Left Diagonal win
    win_O = 0
    win_X = 0
    for i in range(3):
        if new_square[i][i] == 'O':
            win_O += 1
        elif new_square[i][i] == 'X':
            win_X += 1
    
    if win_O == 3 and win_X == 3:
        return "Impossible"
    elif win_O == 3:
        return "O wins"
    elif win_X == 3:
        return "X wins"
    
    # Right Diagonal win
    win_O = 0
    win_X = 0
    for i in range(3):
        j = 3 - (i + 1)
        if new_square[i][j] == 'O':
            win_O += 1
        elif new_square[i][j] == 'X':
            win_X += 1

    if win_O == 3 and win_X == 3:
        return "Impossible"
    elif win_O == 3:
        return "O wins"
    elif win_X == 3:
        return "X wins"

    #Game not finished
    for i in range(3):
        win_ = 0
        for j in range(3):
            if new_square[i][j] == '_':
                win_ += 1
    if win_ > 0:
        return "Game not finished"
    else:
        return "Draw"
    
print(who_won())