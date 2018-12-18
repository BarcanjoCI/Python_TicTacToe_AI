from Board import Board
from Board import PointsAndScores
from Board import Point


# Class that represents AI player
class AiPlayer:
    def __init__(self):
        self.roots_children_scores = []
    
    
    # Returns the best move currently present
    def return_best_move(self):
        maxi = -1000000
        best = None

        for pas in self.roots_children_scores:
            if pas.score > maxi:
                maxi = pas.score
                best = pas.point
        
        return best
    
    # Resets the childreen plays to empty so a new move can be analized and calls the minimax func
    def call_minimax(self, depth, turn, board):
        self.roots_children_scores = []
        self.minimax(depth, turn, board)
        
    
    # Minimax function
    def minimax(self, depth, turn, board):
        if board.has_x_won(): 
            return 1 # AI player has won
        if board.has_o_won(): 
            return -1 # Human player has won
        points_available = board.get_available_points()
        if not points_available: 
            return 0 # No more moves and no win, concludes a draw
        
        scores = [] # List to hold the scores of analized moves
        
        for point in points_available: # Test each available point
            if turn == 1: # AI turn
                board.place_a_move(point, 1)
                current_score = self.minimax(depth + 1, 2, board) # get minimax value for that move
                scores.append(current_score)
                if depth == 0: # If we got back to root depht, add its value to root scores
                    self.roots_children_scores.append(PointsAndScores(point, current_score))
            
            elif turn == 2: # Human turn
                board.place_a_move(point, 2)
                scores.append(self.minimax(depth + 1, 1, board))
            
            board.place_a_move(point, 0)
        
        if turn == 1: # If the turn belong to the AI player, we want the maximum possible score
             return max(int(s) for s in scores)
        else: # If the turn belongs to the human player, AI wants to minimize its score
            return min(int(s) for s in scores)

        

    