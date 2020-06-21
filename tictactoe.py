class TwoHumanPlayers():
  def __init__(self, board):
    self.board = board

  def main(self):
    #Initial board
    self.print_board(self.board)
    moves = 9
    while moves > 0:
      print("Player 1, it's your turn!\n")
      self.validate_move("X", moves)
      if self.who_won(self.board, moves) == "X wins":
        return self.who_won(self.board, moves)
      moves -= 1
      print("Player 2, show us what you got\n")
      self.validate_move("O", moves)
      if self.who_won(self.board, moves) == "O wins":
        return self.who_won(self.board, moves)
      moves -= 1
    return "Draw"

  def print_board(self, board):
    print("---------")
    for line in board:
      new_line = []
      for elem in line:
        if elem == '_':
          new_line.append(" ")
        else:
          new_line.append(elem)
      print("| "+ " ".join(new_line)+" |")
    print("---------")
    
  def validate_move(self, player, moves):
    # Make sure that there is still empty boards
    if moves != 0:
      # Initial input
      #Coordinates follow cartesian graph
      move = input("Enter the coordinates: ").split()
      x = move[0]
      y = move[-1]
      valid_moves = [1, 2, 3]
      # Check if user input is a number
      if not x.isdigit() or not y.isdigit():
        print("You should enter numbers!")
        # Recursion
        self.validate_move(player, moves)
      else:
        x = int(x)
        y = int(y)
        i = 3 - y
        j = x - 1
        # Check if the move chosen is valid
        # coordinates should be between 1 and 3
        # board should be empty
        if x not in valid_moves or  y not in valid_moves:
          print("Coordinates should be from 1 to 3!\n")
          self.validate_move(player, moves)
        elif self.board[i][j] != '_':
          print("This cell is occupied! Choose another one!\n")
          self.validate_move(player, moves)
        else:
          self.board[i][j] = player
          self.print_board(self.board)
                
  def who_won(self, board, moves):
      # Horizontal win
      for line in board:
        if "".join(line) == "XXX":
          return "X wins"
        elif "".join(line) == "OOO":
          return "O wins"
      # Vertical win
      for i in range(3):
        line = ""
        for j in range(3):
          line += board[j][i]
        if line == "XXX":
          return "X wins"
        elif line == "OOO":
          return "O wins"
      
      # \ win
      diagonal1 = board[0][0] + board[1][1] + board[2][2]
      if diagonal1 == "XXX":
        return "X wins"
      elif diagonal1 == "OOO":
        return "O wins"
      
      # / win
      diagonal1 = board[0][2] + board[1][1] + board[2][0]
      if diagonal1 == "XXX":
        return "X wins"
      elif diagonal1 == "OOO":
        return "O wins"
      
new_board = [
              ["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]
              ]

tictactoe_version1 = TwoHumanPlayers(new_board)
print(tictactoe_version1.main())
