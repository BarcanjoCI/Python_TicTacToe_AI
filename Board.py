# Simple point class to create objects that point to positions on the board
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    # Returns a string with the actual point on the board, mainly for debug using print
    def __str__(self):
        return "[x = " + str(self.x + 1) + ", y = " + str(self.y + 1) + "]" 


# Class to associate a point and a score, a dict type could be used instead
class PointsAndScores:
    def __init__(self, point, score):
        self.point = point
        self.score = score


# Class that represents board
# 3x3 board
class Board:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0 ,0]]
        self.available_points = []


    # 0 for empty place, 1 for player 1(AI), 2 for human player
    def get_state(self, point):  
        return self.board[point.x][point.y]


    # Iterate over the board and get all the points where a move can be placed
    def get_available_points(self):
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board[x])):
                if self.board[x][y] == 0:
                    self.available_points.append(Point(x, y)) # If point is avaiable, append it to list
        return self.available_points


    # Places a move by the argument player in the argument point
    def place_a_move(self, point, player):
        self.board[point.x][point.y] = player
    

    # Check if Game is over
    def is_game_over(self):
        return (self.has_o_won() or self.has_x_won() or not self.get_available_points())


    # Check if player o has won 
    def has_o_won(self):
        # Check diagonals for 3 equal values
        if (self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] == 2) \
        or (self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] == 2):
            return True
        
        # Checking for vertical and horizontal values
        for i in range(0, len(self.board)):
            if (self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] == 2) \
            or (self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] == 2):
                return True
        
        return False
    

    # Check if player x has won
    def has_x_won(self):
        # Check diagonals for 3 equal values
        if (self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[0][0] == 1) \
        or (self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[0][2] == 1):
            return True
        
        # Checking for vertical and horizontal values
        for i in range(0, len(self.board)):
            if (self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] and self.board[i][0] == 1) \
            or (self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] and self.board[0][i] == 1):
                return True
        
        return False


    # Displays board on the console
    def display_board(self):
        for row in self.board:
            print("")
            for p in row:
                if p == 0:
                    print(".", end =" ", flush= True) # Empty 
                
                elif p == 1: 
                    print("X", end =" ", flush= True) # PLayer 1

                else:
                    print("O", end =" ", flush= True) # Player 2
        

        print("\n")
    
board = Board()
board.display_board()




    