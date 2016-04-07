import connectfour
import connectfour_module

current_game = connectfour.new_game_state()

print('''Welcome to Connect Four! \nPlease put your moves in one of the following formats: \nDROP # or POP #''')

while True:
    try:
        winner = connectfour.winning_player(current_game)
        if winner == 'R':
            print('Red Player Won!!')
            break
        elif winner == 'Y':
            print('Yellow Player Won!!')
            break

        if current_game.turn == 'R':
            turn = input("Red Player's Turn: ")
        else:
            turn = input("Yellow Player's Turn: ")

        connectfour_module.check_input(turn)
            
        turnlist = turn.split()
        drop_location = int(turnlist[1])

        current_game = connectfour_module.execute_move(current_game, drop_location, turn)

        print(connectfour_module.display(current_game.board))

    except:
        pass
    
    
