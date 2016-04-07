from collections import namedtuple
import connectfour
import connectfour_protocol

class UserInputError(Exception):
    pass

def display(game_board: list)-> str:
    '''
    displays a connect four game board of a given connect four game_state.board
    '''
    result = '1  2  3  4  5  6  7  '
    for num in range(6):
        result += '\n'
        for column in game_board:
            if column[num] == ' ':
                result += '.  '
            elif column[num] == 'R':
                result += 'R  '
            elif column[num] == 'Y':
                result += 'Y  '
    return result

def check_input(user_input: str):
    user_input_list = user_input.split(' ')
    if len(user_input_list) == 2:
        if 'DROP ' in user_input:
            if int(user_input_list[1]) > 0 and int(user_input_list[1]) <= 7:
                pass
            else:
                print('Invalid Move')
                raise UserInputError
        elif 'POP ' in user_input:
            if int(user_input_list[1]) > 0 and int(user_input_list[1]) <= 7:
                pass
            else:
                print('Invalid Move')
                raise UserInputError
        else:
            print('Invalid Move')
            raise UserInputError
    else:
            print('Invalid Move')
            raise UserInputError
    
def execute_move(current_game: namedtuple, drop_location: int, turn: str) -> namedtuple:
    if 'DROP' in turn:
        if drop_location > 0 and drop_location <= 7:
            new_current_game = connectfour.drop_piece(current_game, drop_location - 1)
            return new_current_game
        else:
            raise connectfour.InvalidConnectFourMoveError
    elif 'POP' in turn:
        if drop_location > 0 and drop_location <= 7:
            new_current_game = connectfour.pop_piece(current_game, drop_location - 1)
            return new_current_game
        else:
            raise connectfour.InvalidConnectFourMoveError
    else:
        raise connectfour.InvalidConnectFourMoveError
