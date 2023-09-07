import random
import os
import time
import keyboard

# Размер игрового поля
WIDTH = 10
HEIGHT = 20

# Фигуры для тетриса
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]]
]

# Цвета для отображения фигур
COLORS = ['R', 'G', 'B', 'Y', 'M', 'C', 'W']

# Игровое поле
game_board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Текущая фигура
current_shape = None
current_row = 0
current_col = 0
current_shape_index = 0
current_color = None

# Функция для создания новой фигуры
def new_shape():
    global current_shape, current_row, current_col, current_shape_index, current_color
    current_shape_index = random.randint(0, len(SHAPES) - 1)
    current_shape = SHAPES[current_shape_index]
    current_row = 0
    current_col = WIDTH // 2 - len(current_shape[0]) // 2
    current_color = COLORS[current_shape_index]

# Функция для проверки возможности двигаться вниз
def can_move_down():
    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col] == 1:
                if current_row + row + 1 >= HEIGHT or game_board[current_row + row + 1][current_col + col] != ' ':
                    return False
    return True

# Функция для движения вниз
def move_down():
    global current_row
    if can_move_down():
        current_row += 1
        return True
    else:
        place_shape()
        return False

# Функция для проверки возможности двигаться влево
def can_move_left():
    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col] == 1:
                if current_col + col - 1 < 0 or game_board[current_row + row][current_col + col - 1] != ' ':
                    return False
    return True

# Функция для движения влево
def move_left():
    global current_col
    if can_move_left():
        current_col -= 1

# Функция для проверки возможности двигаться вправо
def can_move_right():
    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col] == 1:
                if current_col + col + 1 >= WIDTH or game_board[current_row + row][current_col + col + 1] != ' ':
                    return False
    return True

# Функция для движения вправо
def move_right():
    global current_col
    if can_move_right():
        current_col += 1

# Функция для проверки возможности поворота фигуры
def can_rotate():
    new_shape_index = (current_shape_index + 1) % len(SHAPES)
    new_shape = SHAPES[new_shape_index]
    for row in range(len(new_shape)):
        for col in range(len(new_shape[row])):
            if new_shape[row][col] == 1:
                if (
                    current_row + row < 0 or
                    current_row + row >= HEIGHT or
                    current_col + col < 0 or
                    current_col + col >= WIDTH or
                    game_board[current_row + row][current_col + col] != ' '
                ):
                    return False
    return True

# Функция для поворота фигуры
def rotate():
    global current_shape_index, current_shape
    if can_rotate():
        current_shape_index = (current_shape_index + 1) % len(SHAPES)
        current_shape = SHAPES[current_shape_index]

# Функция для размещения фигуры на игровом поле
def place_shape():
    global current_row, current_col, current_shape, current_color
    for row in range(len(current_shape)):
        for col in range(len(current_shape[row])):
            if current_shape[row][col] == 1:
                game_board[current_row + row][current_col + col] = current_color
    new_shape()

# Функция для проверки, можно ли начать новую игру
def can_start_new_game():
    for cell in game_board[0]:
        if cell != ' ':
            return False
    return True

# Функция для отображения игрового поля
def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in game_board:
        print(' '.join(row))

# Главный цикл игры
def main():
    new_shape()
    while True:
        if can_start_new_game():
            game_board.clear()
            game_board.extend([[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)])
        if not move_down():
            draw_board()
            continue
        draw_board()
        time.sleep(0.5)

# Запуск игры
if __name__ == "__main__":
    main()
