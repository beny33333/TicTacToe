import random

def init_board():
    if A == ['.','.','.'] and B == ['.','.','.'] and C == ['.','.','.']:
        pass

def get_move():
    global user_coordinate
    global coordinates_list
    coordinates_list = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    
    while True:
        if (len(used_coordinates) == 0) or (len(used_coordinates) == 2) or (len(used_coordinates) == 4) or (len(used_coordinates) == 6) or (len(used_coordinates) == 8):
            user_coordinate = str(input("\nPlayer X insert your coordinate:")).upper()
        else:
            user_coordinate = str(input("\nPlayer 0 insert your coordinate:")).upper()
        if user_coordinate in coordinates_list and user_coordinate not in used_coordinates:
            used_coordinates.append(user_coordinate)
            break
        else:
            print_board()
            print("\nInvalid coordinate or already used!")
            continue 
    return user_coordinate

def get_AI_move():
    global AI_move
    while True:
        AI_move = random.choice(coordinates_list)
        if AI_move not in used_coordinates:
            used_coordinates.append(AI_move)
            break
        else:
            continue

def mark():
    if (len(used_coordinates) == 1) or (len(used_coordinates) == 3) or (len(used_coordinates) == 5) or (len(used_coordinates) == 7) or (len(used_coordinates) == 9):
        mark_istead_of_dot = 'X'
    else:
        mark_istead_of_dot = '0'
    if user_coordinate == 'A1' and A[0] == '.':
        A[0] = mark_istead_of_dot
    if user_coordinate == 'A2' and A[1] == '.':
        A[1] = mark_istead_of_dot
    if user_coordinate == 'A3' and A[2] == '.':
        A[2] = mark_istead_of_dot
    if user_coordinate == 'B1' and B[0] == '.':
        B[0] = mark_istead_of_dot
    if user_coordinate == 'B2' and B[1] == '.':
        B[1] = mark_istead_of_dot
    if user_coordinate == 'B3' and B[2] == '.':
        B[2] = mark_istead_of_dot
    if user_coordinate == 'C1' and C[0] == '.':
        C[0] = mark_istead_of_dot
    if user_coordinate == 'C2' and C[1] == '.':
        C[1] = mark_istead_of_dot
    if user_coordinate == 'C3' and C[2] == '.':
        C[2] = mark_istead_of_dot
    return mark_istead_of_dot

def AI_mark():
    mark_istead_of_dot = '0'
    if AI_move == 'A1' and A[0] == '.':
        A[0] = mark_istead_of_dot
    if AI_move == 'A2' and A[1] == '.':
        A[1] = mark_istead_of_dot
    if AI_move == 'A3' and A[2] == '.':
        A[2] = mark_istead_of_dot
    if AI_move == 'B1' and B[0] == '.':
        B[0] = mark_istead_of_dot
    if AI_move == 'B2' and B[1] == '.':
        B[1] = mark_istead_of_dot
    if AI_move == 'B3' and B[2] == '.':
        B[2] = mark_istead_of_dot
    if AI_move == 'C1' and C[0] == '.':
        C[0] = mark_istead_of_dot
    if AI_move == 'C2' and C[1] == '.':
        C[1] = mark_istead_of_dot
    if AI_move == 'C3' and C[2] == '.':
        C[2] = mark_istead_of_dot
    return mark_istead_of_dot
    
def has_won():
    global win_result
    win_result = [
        [A[0], A[1], A[2]] == ['X','X','X'],
        [B[0], B[1], B[2]] == ['X','X','X'],
        [C[0], C[1], C[2]] == ['X','X','X'],
        [A[0], B[0], C[0]] == ['X','X','X'],
        [A[1], B[1], C[1]] == ['X','X','X'],
        [A[2], B[2], C[2]] == ['X','X','X'],
        [A[0], B[1], C[2]] == ['X','X','X'],
        [A[2], B[1], C[0]] == ['X','X','X'],
        [A[0], A[1], A[2]] == ['O','O','O'],
        [B[0], B[1], B[2]] == ['O','O','O'],
        [C[0], C[1], C[2]] == ['O','O','O'],
        [A[0], B[0], C[0]] == ['O','O','O'],
        [A[1], B[1], C[1]] == ['O','O','O'],
        [A[2], B[2], C[2]] == ['O','O','O'],
        [A[0], B[1], C[2]] == ['O','O','O'],
        [A[2], B[1], C[0]] == ['O','O','O']]
    if any(win_result) is True:
        return True
    else:
        return False

def is_full():
    if not '.' in A and not '.' in B and not '.' in C:
        return True
    else:
        return False

def print_board():
    print(
        '    1     2     3  \n A ' 
         , A[0], ' | ',A[1],' | ',A[2],'\n'
         '  -----+-----+------\n B '
         ,B[0],' | ',B[1],' | ',B[2],'\n'
         '  -----+-----+------\n C '
         ,C[0],' | ',C[1],' | ',C[2],' ')

def print_result():
    if any(win_result[0:8]) == True:
        print_board()
        print("Player X won!")
        main_menu()
    if any(win_result[8:]) == True:
        print_board()
        print("Player 0 won!") 
        main_menu()
    if win_result is False and not '.' in A and not '.' in B and not '.' in C:
        print_board()
        print("It's tie!")
        main_menu()
    else:
        print_board()
        tictactoe_game()
    
def tictactoe_game():
    if game_mode == '1':
        init_board()
        get_move()
        mark()
        has_won()
        is_full()
        print_result()
    if game_mode == '2':
        init_board()
        if (len(used_coordinates) == 0) or (len(used_coordinates) == 2) or (len(used_coordinates) == 4) or (len(used_coordinates) == 6) or (len(used_coordinates) == 8):
            get_move()
            mark()
        else:
            get_AI_move()
            AI_mark()
        has_won()
        is_full()
        print_result()


def main_menu():
    welcome = input("If you want to play TicTacToe game insert 'yes'. If not - 'quit':\n")
    if welcome == 'yes':
        global A
        global B
        global C
        global used_coordinates
        global game_mode
        A = ['.','.','.']
        B = ['.','.','.']
        C = ['.','.','.']
        used_coordinates = []
        game_mode = input('\nChoose a mode:\nMultiplayer - 1\nSingle player - 2:\n')
        print_board()
        tictactoe_game()

if __name__ == "__main__":
    print('Welcome in TicTacToe game! Have fun :)\n')
    main_menu()