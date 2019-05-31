# Requirements:
#   Play tic tac toe
#       Game stops when either player wins, declares winner
#       Game stops when the game is over, declares tie if is tie
#       After game ends, enter 'N' for new game, 'Q' for quit
#       Score is kept track
#           X - 5, O - 2, Tie - 52
def main():
    inputs = [i for i in range(1, 10)]

    

    #       X, O
    wins = [0, 0]

    space = 0
    ties = 0
    inc = 0

    playing = True
    while playing:
        print_board(inputs)
        inc += 1

        # TODO - don't let them play in a square that is already occupied
        space = get_user_input('X')-1
        while inputs[space] == 0 or inputs[space] == -1:
            space = get_user_input('X')-1
        inputs[space] = 0
        print_board(inputs)

        if check_win(inputs):
            print(player_win('X'))
            wins[0] += 1
            print('X - {}, o - {}, Tie - {}'.format(wins[0], wins[1], ties))
            inputs = [i for i in range(1, 10)]
            if play_again() == 'Q':
                playing = False
            continue
            # reset game

        if board_is_full(inputs):
            print('Tie!')
            ties += 1
            print('X - {}, o - {}, Tie - {}'.format(wins[0], wins[1], ties))
            inputs = [i for i in range(1, 10)]
            if play_again() == 'Q':
                playing = False
            continue
            # reset game

        space = get_user_input('o')-1
        while inputs[space] == 0 or inputs[space] == -1:
            space = get_user_input('o') - 1
        inputs[space] = -1
        print_board(inputs)

        if check_win(inputs):
            print(player_win('o'))
            wins[1] += 1
            print('X - {}, o - {}, Tie - {}'.format(wins[0], wins[1], ties))
            inputs = [i for i in range(1, 10)]
            if play_again() == 'Q':
                playing = False
            continue
            # reset game

        

    # TODO - make tic tac toe game


def print_board(arr):
    p = []
    for a in arr:
        p.append(check_val(a))

    print(' {} | {} | {} '.format(p[0], p[1], p[2]))
    print('-----------')
    print(' {} | {} | {} '.format(p[3], p[4], p[5]))
    print('-----------')
    print(' {} | {} | {} '.format(p[6], p[7], p[8]))

def check_win(arr):
    p1 = check_val(arr[0])
    p2 = check_val(arr[1])
    p3 = check_val(arr[2])
    p4 = check_val(arr[3])
    p5 = check_val(arr[4])
    p6 = check_val(arr[5])
    p7 = check_val(arr[6])
    p8 = check_val(arr[7])
    p9 = check_val(arr[8])

    if p1 == p2 == p3:
        return True
    elif p4 == p5 == p6:
        return True
    elif p7 == p8 == p9:
        return True
    elif p1 == p4 == p7:
        return True
    elif p2 == p5 == p8:
        return True
    elif p3 == p6 == p9:
        return True
    elif p1 == p5 == p9:
        return True
    elif p3 == p5 == p7:
        return True
    else:
        return False

def player_win(player):
    return '{} wins!'.format(player)

def play_again():
    resp = 'Q'

    resp = input('Enter N to play again, Q to quit')
    while resp not in {'Q', 'N'}:
        resp = input('Enter N to play again, Q to quit')
    return resp

def check_val(val):
    if val == 0:
        return 'X'
    elif val == -1:
        return 'o'

    return val

def board_is_full(inputs):
    for i in inputs:
        if i > 1:
            return False

    return True

def get_user_input(player):
    num = 0

    num = get_input_int('Place an {} in spot: '.format(player))
    while num > 9 or num < 0:
        num = get_input_int('Place an {} in spot: '.format(player))
    return num

def get_input_int(msg):
    try:
        return int(input(msg))
    except:
        print('Please enter a valid spot')
        return get_input_int(msg)

if __name__ == '__main__':
    main()