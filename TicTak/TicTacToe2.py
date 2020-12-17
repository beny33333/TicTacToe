


A = ['.','.','.']
B = ['.','.','.']
C = ['.','.','.']
LISTA = [A,B,C]

# def lista():
#     global A
#     global B
#     global C
#     global LIST
#     A = ['.','.','.']
#     B = ['.','.','.']
#     C = ['.','.','.']
#     LIST = [A,B,C] 

def init_board():
    if A == ['.','.','.'] and B == ['.','.','.'] and C == ['.','.','.']:
        print_board()
    
   
    # if A == ['.','.','.'] and B == ['.','.','.'] and C == ['.','.','.']:
    #     print_board()
    # if (A != ['.','.','.'] or B != ['.','.','.'] or C != ['.','.','.']) and any(win_result) is False:
    #     print_board()
    # # if (A != ['.','.','.'] or B != ['.','.','.'] or C != ['.','.','.']) and any(win_result) is True:
    # #     A[0] = '.' and A[1] = '.' and A[2] = '.' and B[0] = '.' and B[1] = '.' and B[2] = '.' and C[0] = '.' and C[1] = '.' and C[2] = '.'
    # #     print_board()
    # return A,B,C


def get_move():
    global literaki
    global used_coordinates
    global coordinates_list
    coordinates_list = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    used_coordinates = []
    
    literaki = str(input("Wprowadź koordynaty:"))
    
    while literaki.upper() in coordinates_list and literaki.upper() not in used_coordinates:
        used_coordinates.append(literaki)
    return literaki

def mark():
    # D = ['X','0','X','0','X','0','X','0','X']
    # PlayerX = D[0], D[2], D[4], D[6], D[8]
    # Player0 = D[1], D[3], D[5], D[7]
    # print(PlayerX)
    mark_istead_of_dot = ('X' or '0')
    if literaki == 'A1' and A[0] == '.':
        A[0] = mark_istead_of_dot
    if literaki == 'A2' and A[1] == '.':
        A[1] = mark_istead_of_dot
    if literaki == 'A3' and A[2] == '.':
        A[2] = mark_istead_of_dot
    if literaki == 'B1' and B[0] == '.':
        B[0] = mark_istead_of_dot
    if literaki == 'B2' and B[1] == '.':
        B[1] = mark_istead_of_dot
    if literaki == 'B3' and B[2] == '.':
        B[2] = mark_istead_of_dot
    if literaki == 'C1' and C[0] == '.':
        C[0] = mark_istead_of_dot
    if literaki == 'C2' and C[1] == '.':
        C[1] = mark_istead_of_dot
    if literaki == 'C3' and C[2] == '.':
        C[2] = mark_istead_of_dot
    if literaki not in coordinates_list and literaki in used_coordinates:
        return None
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
        print("Wygrał gracz X!")
        main_menu()
    if any(win_result[8:]) == True:
        print_board()
        print("wygrał gracz O") 
        main_menu()
    if win_result is False and not '.' in A and not '.' in B and not '.' in C:
        print_board()
        print("It's tie")
        main_menu()
    else:
        print_board()
        main()
    
def main():
    # LISTA = [A,B,C]
    init_board()
    # if ('X' or '0') in (A or B or C):
    get_move()
    mark()
    has_won()
    is_full()
    print_result()

def main_menu():
    Tryb_gry = input('Jeśli chcesz zagrać sam ze sobą to se graj i napisz yes or no : ''\n')
    if Tryb_gry == 'yes':
        # A[0] == '.' and A[1] == '.' and A[2] == '.' and B[0] == '.' and B[1] == '.' and B[2] == '.' and C[0] == '.' and C[1] == '.' and C[2] == '.'
        main()
    # else:
    #     main_menu()


if __name__ == "__main__":
    main_menu()




    # D = [X,0,X,0,X,0,X,0,X]
    # Player X = D[0], D[2], D[4], D[6], D[8]
    # Player 0 = D[1,3,5,7]
    # print Player X


# init_board(LISTA)
# get_move(coordinates_list, used_coordinates)










# init_board()
# get_move()
# mark()
# has_won()
# is_full()
# print_board()
# print_result()