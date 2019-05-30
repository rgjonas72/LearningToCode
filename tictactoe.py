# Requirements:
#   Play tic tac toe
#       Game stops when either player wins, declares winner
#       Game stops when the game is over, declares tie if is tie
#       After game ends, enter 'N' for new game, 'Q' for quit
#       Score is kept track
#           X - 5, O - 2, Tie - 52
def main():
    
    inputs = [1,2,3,4,5,6,7,8,9]
    print_board(inputs)
    xwins = 0
    ywins = 0
    ties = 0
    inc = 0
    nq = '43 sucks'
    for x in range(5):
        inc += 1
        t = get_user_input_x()-1
        inputs[t] = 0
        print_board(inputs)
        if checkwin(inputs):
            print(xwin())
            xwins += 1
            break
        if inc == 5:
            print('Tie!')
            ties += 1
            break
        t = get_user_input_y()-1
        inputs[t] = -1
        print_board(inputs)
        if checkwin(inputs):
            print(ywin())
            inc = -1
            ywins += 1
            break

    print('X - {}, o - {}, Tie - {}'.format(xwins, ywins, ties))
    nq = playagain()
    if nq == 'N':
        main()

    # TODO - make tic tac toe game

def print_board(arr):
    p1 = checkval(arr[0])
    p2 = checkval(arr[1])
    p3 = checkval(arr[2])
    p4 = checkval(arr[3])
    p5 = checkval(arr[4])
    p6 = checkval(arr[5])
    p7 = checkval(arr[6])
    p8 = checkval(arr[7])
    p9 = checkval(arr[8])

    print(' {} | {} | {} '.format(p1, p2, p3))
    print('-----------')
    print(' {} | {} | {} '.format(p4, p5, p6))
    print('-----------')
    print(' {} | {} | {} '.format(p7, p8, p9))

def checkwin(arr):
    p1 = checkval(arr[0])
    p2 = checkval(arr[1])
    p3 = checkval(arr[2])
    p4 = checkval(arr[3])
    p5 = checkval(arr[4])
    p6 = checkval(arr[5])
    p7 = checkval(arr[6])
    p8 = checkval(arr[7])
    p9 = checkval(arr[8])

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
    #elif all(x < 1 for x in arr):
     #   return True
    else:
        return False

def xwin():
    return 'X wins!'

def ywin():
    return 'o wins!'

def playagain ():
    try:
        return (input('Enter N to play again, Q to quit'))
    except:
        print('Please enter a valid response')
        return playagain()
        

def checkval (val):
    if val == 0:
        return 'X' 
    elif val == -1:
        return 'o'
    else:
        return val

def get_user_input_x():
    try:
        return int(input('Place an X in spot: '))
    except:
        print('Please enter a valid spot')
        return get_user_input_x()

def get_user_input_y():
    try:
        return int(input('Place an o in spot: '))
    except:
        print('Please enter a valid spot')
        return get_user_input_y()

if __name__ == '__main__':
    main()