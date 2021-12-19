import cells
import random
import pygame
from PIL import Image

import options


def generate_pool(x, y):
    return [[cells.cell('empty', i, j) for i in range(x)] for j in range(y)]


def pool_check(pool):  # метод необходим для тестирования, в основной программе не использовался
    reversepool = [pool[len(pool) - 1 - i] for i in range(len(pool))]
    for i in reversepool:
        for j in i:
            print(f'{j.color}', end=' ')
        print()


def pool_size(pool):  # return max x + 1 max y + 1
    return len(pool[0]), len(pool)


def getcell(pool, x, y):  # вернуть объект класса Cell
    return pool[y][x]


def can_fall(pool, x, y):  # проверка на возможность фигуры падения (под нами нет фигур и 0 высоты)
    max_x, max_y = pool_size(pool)
    if 0 <= y - 1 <= max_y - 1:
        if getcell(pool, x % max_x, y - 1).color == 'empty' or getcell(pool, x % max_x, y - 1).color == getcell(pool, x % max_x, y).color:
            return True
    return False


def generate_shape(pool, shape, x, y, color, turn):  # создать на доске фигуру и вернуть доску с фигурой
    cells_to_fill = cells.shape(shape, x, y, color, turn).shape()
    for i in cells_to_fill:
        getcell(pool, i[0] % len(pool[0]), i[1]).color = color
    return pool


def generate_color_rgb():  # вернуть кортеж из 3 случайных значений 0-255
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def generate_pool_img(pool):  # возвращает Surface поверхность, основанную на PIL Image, основанной на доске
    width, height = pool_size(pool)[0] * options.cell_size, pool_size(pool)[1] * options.cell_size
    img = Image.new('RGB', (width, height))
    for i in range(0, height, options.cell_size):
        for j in range(0, width, options.cell_size):
            if getcell(pool, j // options.cell_size, i // options.cell_size).color == 'empty':
                img.paste(Image.new('RGB', (options.cell_size, options.cell_size), 'white'), (j, i))
            else:
                img.paste(Image.new('RGB', (options.cell_size, options.cell_size),
                                    getcell(pool, j // options.cell_size, i // options.cell_size).color), (j, i))
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    return pygame.image.fromstring(img.tobytes(), img.size, img.mode).convert()


def save_load():  # загрузить сохранение save.txt в игру
    pool = []
    index = 0
    for line in open('save.txt'):
        if index == 0 and line == 'None':
            return
        if index == 0:
            score = int(line)
        if index > 0:
            y = [i for i in line.split('|')]
            y.remove('\n')
            for i in range(len(y)):
                x = y[i].split()
                if x[2] == 'empty':
                    y[i] = cells.cell('empty', int(x[0]), int(x[1]))
                else:
                    y[i] = cells.cell((int(x[2]), int(x[3]), int(x[4])), int(x[0]), int(x[1]))
            pool.append(y)
        index += 1
    return pool, score


def save_save(pool, score):  # загрузить в сохранение save.txt игру
    save_file = open('save.txt', 'w')
    save_file.write(str(score))
    save_file.write('\n')
    for y in pool:
        for x in y:
            if x.color == 'empty':
                save_file.write(f'{x.x} {x.y} empty|')
            else:
                save_file.write(f'{x.x} {x.y} {x.color[0]} {x.color[1]} {x.color[2]}|')
        save_file.write('\n')




