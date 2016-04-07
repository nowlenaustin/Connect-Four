import connectfour
import connectfour_module
import connectfour_protocol

while True:
    try:
        host = input('Please enter the host: ')
        port = int(input('Please enter the port: '))

        print('Connecting...')
        connection = connectfour_protocol.connect(host, port)
        print('Connected')
        break
    except:
        print('Connection Failed.')
        pass

current_game = connectfour.new_game_state()

class UsernameError(Exception):
    pass

while True:
    try:
        username = input("Enter Username: ")
        if ' ' in username:
            print('Invalid Username')
            raise UsernameError
        else:
            break
    except:
        pass
    
connectfour_protocol.hello(connection, username)

print('''Welcome to Connect Four! \nPlease put your moves in one of the following formats: \nDROP # or POP #''')
while True:
    try:
        user_turn = input("Enter Move: ")
        connectfour_module.check_input(user_turn)
        user_turn_list = user_turn.split()
        user_drop_location = int(user_turn_list[1])
        current_game = connectfour_module.execute_move(current_game, user_drop_location, user_turn)
        winner_check = connectfour_protocol.send(connection, user_turn, current_game) #also sends user move to server

        if winner_check != None:
            break

        print("\nYour Move: " + user_turn)
        print(connectfour_module.display(current_game.board) + '\n')

        server_turn = connectfour_protocol.server_move(connection)
        server_turn_list = server_turn.split()
        server_drop_location = int(server_turn_list[1])
        current_game = connectfour_module.execute_move(current_game, server_drop_location, server_turn)
        
        print("Server's Move: " + server_turn)
        print(connectfour_module.display(current_game.board) + '\n')

        if connectfour_protocol.ready(connection) != '':
            break
    
    except:
        pass
    
connectfour_protocol.close(connection)
print('Connection Closed. \nThanks for playing!')
