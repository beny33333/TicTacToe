A = ['.','.','.']
B = ['.','.','.']
C = ['.','.','.']
result_list = []
LISTA = [A,B,C]
list_to_dictionary = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
win_result = [[A[0], A[1], A[2]] == ['X','X','X'],
    [B[0], B[1], B[2]] == ['X','X','X'],
    [C[0], C[1], C[2]] == ['X','X','X'],
    [A[0], B[0], C[0]] == ['X','X','X'],
    [A[1], B[1], C[1]] == ['X','X','X'],
    [A[2], B[2], C[2]] == ['X','X','X'],
    [A[0], B[1], C[2]] == ['X','X','X'],
    [A[2], B[1], C[0]] == ['X','X','X']]

def init_board():
    print(LISTA)


def get_move():
    while True:
        guess = str(input('Please dawaj koordynaty gościu!')).upper()
        if guess in list_to_dictionary and guess == 'A1' and guess not in result_list:
            A[0] = 'X'
        if guess in list_to_dictionary and guess == 'A2' and guess not in result_list:
            A[1] = 'X'
        if guess in list_to_dictionary and guess == 'A3' and guess not in result_list:
            A[2] = 'X'
        if guess in list_to_dictionary and guess == 'B1' and guess not in result_list:
            B[0] = 'X'
        if guess in list_to_dictionary and guess == 'B2' and guess not in result_list:
            B[1] = 'X'
        if guess in list_to_dictionary and guess == 'B3' and guess not in result_list:
            B[2] = 'X'
        if guess in list_to_dictionary and guess == 'C1' and guess not in result_list:
            C[0] = 'X'
        if guess in list_to_dictionary and guess == 'C2' and guess not in result_list:
            C[1] = 'X'
        if guess in list_to_dictionary and guess == 'C3' and guess not in result_list:
            C[2] = 'X'
        elif guess not in list_to_dictionary or guess in result_list:
            print('NT dude, try again')
        if guess not in result_list and guess in list_to_dictionary:
            result_list.append(guess)
        print(LISTA)
        return result_list





# def get_ai_move()

# def mark():

def has_won():
    if any(win_result) is True:
        print("Wygrałeś!")
        return True
    else:
        return False



def is_full():
    if '.' in LISTA:
        return False
    else:
        return True

init_board()
get_move()
has_won()
is_full()

# def print_board():

# def print_result():

# def tictactoe_game():

# def main_menu()

# def quit():

# if name == "tictactoe_game":
#     tictactoe_game()