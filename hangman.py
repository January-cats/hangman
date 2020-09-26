# -*- coding:utf-8 -*-

def hangman(word):
    wrong = 0
    stages = [
    "",
    "_____     ",
    "|         ",
    "|    |    ",
    "|    0    ",
    "|   /|\   ",
    "|   / \   ",
    "|         "
    ]
    rletters = list(word) #残っている文字
    board = ["_"] * len(word) #文字列リスト、正解の文字のヒントを描画する
    win = False
    print("Welcome to Hangman!")
    while wrong < len(stages) - 1:
        print('\n')
        message = '１文字を入力してね'
        char = input('{}: '.format(message))
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print('You won!')
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose!")
        print("The answer was: {}".format(word))

if __name__ == '__main__':
    hangman('cat')
