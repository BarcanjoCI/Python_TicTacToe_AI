from Board import Board, Point
from AiPlayer import AiPlayer
import sys

ai_player = AiPlayer()
board = Board()
board.display_board()

print("Who makes the first move? (1)Computer (2)You")
choice = int(input())

if(choice == 1):
    ai_player.call_minimax(0, 1, board)
    for pas in ai_player.roots_children_scores:
        print("Point: ", end="")
        print(pas.point, end="")
        print(" Score: " + str(pas.score))
    board.place_a_move(ai_player.return_best_move(), 1)
    board.display_board()


while not board.is_game_over():
    print("Your move? row (1, 2 or 3), column (1, 2 or 3)")
    x = int(input("row?"))
    y = int(input("col?"))
    user_point = Point(x - 1, y - 1)

    while(not board.get_state(user_point) == 0):
        print("Invalid Move, try again: ")
        x = int(input("row?"))
        y = int(input("col?"))
        user_point = Point(x - 1, y - 1)

    board.place_a_move(user_point, 2)
    board.display_board()

    if board.is_game_over():
        break
    
    ai_player.call_minimax(0, 1, board)
    for pas in ai_player.roots_children_scores:
        print("Point: ", end="")
        print(pas.point, end="")
        print(" Score: " + str(pas.score))
    board.place_a_move(ai_player.return_best_move(), 1)
    board.display_board()
    
if board.has_x_won():
    print("You got rekt son!")
    
elif board.has_o_won():
    print("You win... This Time")
    
else:
    print("Draws aren't fun :c")


    
