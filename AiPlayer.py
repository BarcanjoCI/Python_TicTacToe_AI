from Board import Board

# Class that represents AI player
class AiPlayer:
    def __init__(self):
        self.rootsChildrenScores = []
        self.availablePoints = []
        self.board = Board()