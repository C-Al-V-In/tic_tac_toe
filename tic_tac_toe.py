oxs = '         '
chess_pieces = ['X', 'O']
turns = 0
win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def game():
    while True:
        move()
        check()
        if turns == 9:  # 若第9回合仍无结果就和
            break


def show():  # 展示棋盘
    print('---------')
    for i in range(3):
        print('|', ' '.join(oxs[i * 3:i * 3 + 3]), '|')
    print('---------')


def check():  # 检查对局情况
    for i in range(0, 7):
        if oxs[win[i][0]] == oxs[win[i][1]] == oxs[win[i][2]] == 'O':
            print('O wins')
            exit()
        elif oxs[win[i][0]] == oxs[win[i][1]] == oxs[win[i][2]] == 'X':
            print('X wins')
            exit()


def move():
    print('Enter the coordinates:')
    while True:
        coordinates = input().split()
        y, x = coordinates
        serial_number = int(y) * 3 + int(x) - 4
        global oxs
        if x not in ['1', '2', '3'] or y not in ['1', '2', '3']:
            if not x.isdigit() or not y.isdigit():
                print('You should enter numbers!')
            elif int(x) < 1 or int(y) < 1 or int(x) > 3 or int(x) > 3:
                print('Coordinates should be from 1 to 3!')
        else:
            if oxs[serial_number] == 'O' or oxs[serial_number] == 'X':
                print('This cell is occupied! Choose another one!')
            else:
                global turns
                oxs = oxs[:serial_number] + chess_pieces[turns % 2] + oxs[serial_number + 1:]  # 用回合数的奇偶区分棋子
                turns += 1
                show()
                break


if __name__ == '__main__':
    show()
    game()
