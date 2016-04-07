import socket
import connectfour_module
from collections import namedtuple

ConnectFourConnection = namedtuple('ConnectFourConnection', ['socket', 'socket_in', 'socket_out'])

class ConnectFourError(Exception):
    pass

def connect(host:str, port:int):
    connectfour_socket = socket.socket()
    
    connectfour_socket.connect((host, port))

    connectfour_socket_in = connectfour_socket.makefile('r')
    connectfour_socket_out = connectfour_socket.makefile('w')

    return ConnectFourConnection(socket = connectfour_socket, socket_in = connectfour_socket_in, socket_out = connectfour_socket_out)

def hello(connection: ConnectFourConnection, username: str):
    _write_line(connection, 'I32CFSP_HELLO ' + username)
    _read_line(connection)
    _write_line(connection, 'AI_GAME')
    _read_line(connection)

def send(connection: ConnectFourConnection, turn: str, current_game: namedtuple):
    _write_line(connection, turn)
    return _expect_line(connection, 'OKAY', current_game)

def server_move(connection: ConnectFourConnection):
    return _read_line(connection)

def ready(connection: ConnectFourConnection):
    line= _read_line(connection)
    if line == 'WINNER_RED':
         print('You Won!!')
         return 'winner red'
    elif line == 'WINNER_YELLOW':
        print('You lost... AI won.')
        return 'winner yellow'
    else:
        return ''

def close(connection: ConnectFourConnection):
    connection.socket_in.close()
    connection.socket_out.close()
    connection.socket.close()

def _read_line(connection: ConnectFourConnection) -> str:
    return connection.socket_in.readline()[:-1]

def _expect_line(connection: ConnectFourConnection, expected: str, current_game: namedtuple):
    line = _read_line(connection)
    if line == 'WINNER_RED':
        print(connectfour_module.display(current_game.board) + '\n')
        print('You Won!!')
        return 'WINNER_RED'
    elif line == 'WINNER_YELLOW':
        print('You lost... Server Won.')
        return 'WINNER_YELLOW'
    elif line != expected:
        raise ConnectFourError()
    else:
        return None


def _write_line(connection: ConnectFourConnection, line: str):
    connection.socket_out.write(line + '\r\n')
    connection.socket_out.flush()
