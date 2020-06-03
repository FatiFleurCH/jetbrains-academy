# write your code here
new_square = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]

def print_square(square):
  print("---------")
  for line in square:
    new_line = []
    for elem in line:
      if elem == '_':
        new_line.append(" ")
      else:
        new_line.append(elem)
    print("| "+ " ".join(new_line)+" |")
  print("---------")
def validate_move(player, moves):
  if moves != 0:
    move = input("Enter the coordinates: ").split()
    x = move[0]
    y = move[-1]
    valid_moves = [1, 2, 3]
    if not x.isdigit() or not y.isdigit():
      print("You should enter numbers!")
      validate_move(player, moves)
    else:
      x = int(x)
      y = int(y)
      i = 3 - y
      j = x - 1
      if x not in valid_moves or  y not in valid_moves:
        print("Coordinates should be from 1 to 3!")
        validate_move(player, moves)
      elif new_square[i][j] != '_':
        print("This cell is occupied! Choose another one!")
        validate_move(player, moves)
      else:
        new_square[i][j] = player
        print_square(new_square)
def check_win(win_O, win_X):
    if win_O == 3 and win_X == 3:
        return "Impossible"
    elif win_O == 3:
        return "O wins"
    elif win_X == 3:
        return "X wins"
    else:
        return "Nothing much"
def who_won(square, moves):
    # Horizontal win
    for line in square:
      if "".join(line) == "XXX":
        return "X wins"
      elif "".join(line) == "OOO":
        return "O wins"
    # Vertical win
    reversed_square = []
    for i in range(3):
      line = ""
      for j in range(3):
        line += square[i][j]
      reversed_square.append(line)
    for line in square:
      if line == "XXX":
        return "X wins"
      elif line == "OOO":
        return "O wins"
    
    # \ win
    diagonal1 = square[0][0] + square[1][1] + square[2][2]
    if diagonal1 == "XXX":
      return "X wins"
    elif diagonal1 == "OOO":
      return "O wins"
    
    # / win
    diagonal1 = square[0][2] + square[1][1] + square[2][0]
    if diagonal1 == "XXX":
      return "X wins"
    elif diagonal1 == "OOO":
      return "O wins"
    
    #Draw
    if moves == 0:
      return "Draw"
    
#Initial square
print_square(new_square)
moves = 9
while moves > 0:
  validate_move("X", moves)
  if who_won(new_square, moves) == "X wins" or who_won(new_square, moves) == "O wins" or who_won(new_square, moves) == "Draw":
    print(who_won(new_square, moves))
    break
  moves -= 1
  validate_move("O", moves)
  if who_won(new_square, moves) == "X wins" or who_won(new_square, moves) == "O wins" or who_won(new_square, moves) == "Draw":
    print(who_won(new_square, moves))
    break
  moves -= 1
