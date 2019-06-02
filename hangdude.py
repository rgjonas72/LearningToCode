from random_word import RandomWords
class hangdude:
    def __init__(self):
        self.r = RandomWords()
    
    def choose_random_word(self):
        
        return list(self.r.get_random_word())

    def guess_letter(self):
        letter = input('Guess a letter: ')
        while len(letter) == 0 or len(letter) > 1:
            letter = input('Guess a letter: ')
        return letter

    def check_guess(self, letter, word):
        self.correct_spaces = []
        for i in range(len(word)):
            if letter == word[i]:
                self.correct_spaces.append(i)
        return self.correct_spaces

    def draw_hangdude(self, failcounter):
        if failcounter == 0:
            print(' |------')
            print(' |      ')
            print(' |      ')
            print(' |      ')
            print('---')
        elif failcounter == 1:
            print(' |------')
            print(' |     o')
            print(' |      ')
            print(' |      ')
            print('---')
        elif failcounter == 2:
            print(' |------')
            print(' |     o')
            print(' |     |')
            print(' |      ')
            print('---')
        elif failcounter == 3:
            print(' |------')
            print(' |     o')
            print(' |    \|')
            print(' |      ')
            print('---')
        elif failcounter == 4:
            print(' |------')
            print(' |     o')
            print(' |    \|/')
            print(' |      ')
            print('---')
        elif failcounter == 5:
            print(' |------')
            print(' |     o')
            print(' |    \|/')
            print(' |    / ')
            print('---')
        elif failcounter == 6:
            print(' |------')
            print(' |     o')
            print(' |    \|/')
            print(' |    / \\')
            print('---')
            print('You lose idiot!')

    def create_empty_board(self, word):
        self.board = []
        for i in word:
            self.board.append(' _ ')
        return self.board

    def print_board(self, board):
        return ''.join(board)

    def play_game(self):
        word = self.choose_random_word()
        print(word)
        board = self.create_empty_board(word)
        print(self.print_board(board))
        failcounter = 0
        playing = True
        while playing:
            guess = self.guess_letter()
            self.check_guess(guess, word)
            check = self.check_guess(guess,word)
            if (len(check)) == 0:
                print('u mssed up')
                failcounter += 1

            else:
                for i in range(len(check)):
                    board[check[i]] = guess
            print(self.print_board(board))
            print()
            self.draw_hangdude(failcounter)
            if board == word:
                print('You win!')
                break
            if failcounter == 6:
                break
        return ''


def main():
    hangman = hangdude()
    print(hangman.play_game())

if __name__ == '__main__':
    main()