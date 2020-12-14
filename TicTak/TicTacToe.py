A = ['.','.','.']
B = ['.','.','.']
C = ['.','.','.']


result_list = []
LISTA = [A,B,C]
list_to_dictionary = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
lista1 = ['X','O']
znak = lista1[0] or lista1[1]

def win_condition():
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
    return win_result

def init_board():
    print_board()
    
def get_move():
    global ruchy
    ruchy = 9
    while ruchy > 0:
        guess = input("Wprowadź koordynaty").upper()

        if ruchy == 9:
            znak = lista1[0]
        if ruchy == 8:
            znak = lista1[1]
        if ruchy == 7:
            znak = lista1[0]
        if ruchy == 6:
            znak = lista1[1]  
        if ruchy == 5:
            znak = lista1[0]
        if ruchy == 4:
            znak = lista1[1]  
        if ruchy == 3:
            znak = lista1[0]
        if ruchy == 2:
            znak = lista1[1]  
        if ruchy == 1:
            znak = lista1[0]

        if guess in list_to_dictionary and guess == 'A1' and guess not in result_list:
            A[0] = znak
        if guess in list_to_dictionary and guess == 'A2' and guess not in result_list:
            A[1] = znak
        if guess in list_to_dictionary and guess == 'A3' and guess not in result_list:
            A[2] = znak
        if guess in list_to_dictionary and guess == 'B1' and guess not in result_list:
            B[0] = znak
        if guess in list_to_dictionary and guess == 'B2' and guess not in result_list:
            B[1] = znak
        if guess in list_to_dictionary and guess == 'B3' and guess not in result_list:
            B[2] = znak
        if guess in list_to_dictionary and guess == 'C1' and guess not in result_list:
            C[0] = znak
        if guess in list_to_dictionary and guess == 'C2' and guess not in result_list:
            C[1] = znak
        if guess in list_to_dictionary and guess == 'C3' and guess not in result_list:
            C[2] = znak
        if guess not in list_to_dictionary or guess in result_list:
            print('NT dude, try again')
        if guess not in result_list and guess in list_to_dictionary:
            result_list.append(guess)   
            ruchy -=1
        if win_condition() is True:   
            print_board
        else:
            print_board()


def has_won():
    if any(win_result) == True:
        return True
    if any(win_result) != True:
        return False

def is_full():
    if not '.' in A and B and C:
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
    if has_won() is True:
        print_result()
    if has_won() is False:
        print_result()
    while any('.') in A and B and C:
        return get_move()
        


def print_result():
    if has_won() is True and any(win_result[0:8]) == True:
        print("Wygrał gracz X!")
    if has_won() is True and any(win_result[8:]) == True:
        print("wygrał gracz O") 
    if has_won() is False and is_full() is True:
        print("It's tie")
        

# def tictactoe_game():

# def main_menu()



# def quit():
#     literaki = input("Wód ju plej egen? yes or quit mtf")
#         if literaki =

# if name == "tictactoe_game":
#     tictactoe_game()

win_condition()
init_board()
get_move()
is_full()
