import cells
import options
import methods
import random
import pygame

if methods.save_load() is None:
    pool = methods.generate_pool(options.x_size, options.y_size)
    score = 0
else:
    pool, score = methods.save_load()

pygame.mixer.init()
move_sound = pygame.mixer.Sound('move_sound.mpeg')
move_sound.set_volume(options.volume/10)
score_sound = pygame.mixer.Sound('score_sound.mpeg')
score_sound.set_volume(options.volume)
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(options.music_volume)


def left_arrow():
    global pool, x, y, turn, color, shape
    pool = methods.generate_shape(pool, shape, x, y, 'empty', turn)
    x -= 1
    pool = methods.generate_shape(pool, shape, x, y, color, turn)


def right_arrow():
    global pool, x, y, turn, color, shape
    pool = methods.generate_shape(pool, shape, x, y, 'empty', turn)
    x += 1
    pool = methods.generate_shape(pool, shape, x, y, color, turn)


def down_arrow():
    global pool, x, y, turn, color, shape
    pool = methods.generate_shape(pool, shape, x, y, 'empty', turn)
    y -= 1
    pool = methods.generate_shape(pool, shape, x, y, color, turn)


def space():
    global pool, x, y, turn, color, shape
    pool = methods.generate_shape(pool, shape, x, y, 'empty', turn)
    turn = (turn + 1) % 4
    pool = methods.generate_shape(pool, shape, x, y, color, turn)


pygame.init()  # инициализация библиотеки
pygame.display.set_caption('tetris')  # название окна
width, height = methods.pool_size(pool)[0] * options.cell_size + 200, methods.pool_size(pool)[1] * options.cell_size
screen = pygame.display.set_mode((width, height))  # размеры окна
clock = pygame.time.Clock()  # объект, необходимый для отслеживания времени

scoreboard = [int(line) for line in open('scoreboard.txt')]  # загрузка в список данных из файла с рекордами
while len(scoreboard) < 10:
    scoreboard.append(0)

shape = random.choice(['o', 'i', 'j', 'l', 'z', 't', 's'])
x = len(pool[0]) // 2
y = len(pool) - 2
color = methods.generate_color_rgb()
turn = 0
new_shape = random.choice(['o', 'i', 'j', 'l', 'z', 't', 's'])
new_color = methods.generate_color_rgb()
methods.generate_shape(pool, shape, x, y, color, turn)  # создание фигуры и вывод её на игровую доску

update = 0  # данная переменная будет аккумулироваться
# при достижении своего максимума будет насильно толкать фигуру вниз

pause = True  # установка игры в режим пауза
run = True  # пока run, наше окно будет видно пользователю
while run:
    clock.tick(options.fps)  # данный метод контролирует частоту обновления экрана, игровой логики
    # и самого цикла while run

    i = 0  # проверка поля от высоты поля = 0 и до верхушки
    while i < len(pool) and not pause:
        destroy = True
        for j in range(len(pool[i])):
            if pool[i][j].color == 'empty':  # если строка полностью заполнена частями фигур
                destroy = False
                break
        if destroy:
            for j in pool[i]:
                j.color = 'empty'  # то она будет удалять из себя все части фигур
            for j in range(i, len(pool) - 1):  # видимость того, что после удаления нижней строки,
                # верхние строки будут "падать"
                pool[j], pool[j + 1] = pool[j + 1], pool[j]
            score += 1
            i = -1
            score_sound.play()  # проигрывание звука
        i += 1

    end = False  # проверка на то, что игра закончилась
    for j in cells.shape(shape, x, y, color, turn).shape():  # cells.shape.shape() возвращает список кортежей (x,y)
        # которые вместе собирают готовую фигуру на доске
        if not methods.can_fall(pool, j[0], j[1]):  # если текущая фигура не может упасть ниже
            # например под нами фигура или высота 0
            shape = new_shape
            x = len(pool[0]) // 2
            y = len(pool) - 2
            color = new_color
            turn = 0
            new_shape = random.choice(['o', 'i', 'j', 'l', 'z', 't', 's'])
            new_color = methods.generate_color_rgb()
            can = True  # если фигура может создасться, то она создается
            # если не может, то игра заканчивается
            for i in cells.shape(shape, x, y, color, turn).shape():
                if pool[i[1]][i[0] % len(pool[i[1]])].color != 'empty' and pool[i[1]][i[0] % len(pool[i[1]])].color != color:
                    can = False
                    break
            if can:
                pool = methods.generate_shape(pool, shape, x, y, color, turn)
                break
            else:
                end = True
                pause = True
                break

    for event in pygame.event.get():  # список ивентов pygame
        if event.type == pygame.QUIT:  # если окно закрывается/нажат красный крест
            run = False
        if event.type == pygame.KEYDOWN:  # если кнопка нажалась

            if event.key == pygame.K_ESCAPE:
                if pause:
                    pause = False
                else:
                    pause = True

            if event.key == pygame.K_SPACE:
                can = True
                for i in cells.shape(shape, x, y, color, (turn + 1) % 4).shape():
                    if pool[i[1]][i[0] % len(pool[i[1]])].color != 'empty' and pool[i[1]][i[0] % len(pool[i[1]])].color != color:
                        can = False
                        break
                if can and not pause:
                    space()

            if event.key == pygame.K_RIGHT:
                can = True
                for i in cells.shape(shape, x + 1, y, color, turn).shape():
                    if pool[i[1]][i[0] % len(pool[i[1]])].color != 'empty' and pool[i[1]][i[0] % len(pool[i[1]])].color != color:
                        can = False
                        break
                if can and not pause:
                    right_arrow()

            if event.key == pygame.K_LEFT:
                can = True
                for i in cells.shape(shape, x - 1, y, color, turn).shape():
                    if pool[i[1]][i[0] % len(pool[i[1]])].color != 'empty' and pool[i[1]][i[0] % len(pool[i[1]])].color != color:
                        can = False
                        break
                if can and not pause:
                    left_arrow()

            if event.key == pygame.K_DOWN:
                can = True
                while can:
                    if y <= 3:
                        can = False
                    for i in cells.shape(shape, x, y - 1, color, turn).shape():
                        if pool[i[1]][i[0] % len(pool[i[1]])].color != 'empty' and pool[i[1]][i[0] % len(pool[i[1]])].color != color:
                            can = False
                            break
                    if can and not pause:
                        down_arrow()
        if event.type == pygame.MOUSEBUTTONDOWN:  # проверка нажатия мышки в координатах кнопки
            # и при активированной pause
            if pygame.Rect(width // 4, height // 8, 2 * width // 4, height // 8).collidepoint(event.pos) and pause:
                if end:  # если игра была закончена, а наш результат score набрал очков,
                    # достаточных для попадания в scoreboard, то наш score записывается в файл scoreboard.txt
                    if score > scoreboard[9]:
                        scoreboard[9] = score
                        scoreboard.sort(reverse=True)
                        file = open('scoreboard.txt', 'w')
                        for line in scoreboard:
                            file.write(f'{line}\n')
                    pool = methods.generate_pool(options.x_size, options.y_size)
                    shape = random.choice(['o', 'i', 'j', 'l', 'z', 't', 's'])
                    x = len(pool[0]) // 2
                    y = len(pool) - 2
                    color = methods.generate_color_rgb()
                    turn = 0
                    new_shape = random.choice(['o', 'i', 'j', 'l', 'z', 't', 's'])
                    new_color = methods.generate_color_rgb()
                    methods.generate_shape(pool, shape, x, y, color, turn)
                    end = False
                pause = False
            if pygame.Rect(width // 4, 3 * height // 8, 2 * width // 4, height // 8).collidepoint(event.pos) and pause:
                run = False  # при нажатии второй кнопки, игра закрывается
    if not pause:
        if update < options.fps*10 / 4:
            update += 10 + score
        else:
            update = 0
            can = True
            for i in cells.shape(shape, x, y - 1, color, turn).shape():
                if pool[i[1]][i[0] % len(pool[i[1]])].color != 'empty' and pool[i[1]][i[0] % len(pool[i[1]])].color != color:
                    can = False
                    break
            if can:
                down_arrow()
                move_sound.play()

    img = methods.generate_pool_img(pool)  # метод создания изображения, основываясь на цветах доски
    screen.blit(img, (0, 0))  # метод заполнения экрана объектом img, начиная из координат окна (0,0)
    screen.blit(pygame.Surface((200, height)), (width-200, 0))
    screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(f'{score}', False, 'white'), (width-175, 0))
    for i in range(len(scoreboard)):
        screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render(f'{scoreboard[i]}', False, 'white'), (width - 175, 40*(i+1)))
    screen.blit(methods.generate_pool_img(methods.generate_shape(methods.generate_pool(4, 4), new_shape, 2, 1, new_color, 0)), (width-150, height-150))
    pygame.mixer.music.unpause()
    if pause:
        pygame.mixer.music.pause()
        screen.fill('black')
        pygame.draw.rect(screen, 'white', pygame.Rect(width // 4, height // 8, 2 * width // 4, height // 8))
        text = pygame.font.SysFont('Comic Sans MS', height // 26).render('Играть', False, 'black')
        screen.blit(text, text.get_rect(center=(width // 2, 3 * height // 16)))
        pygame.draw.rect(screen, 'white', pygame.Rect(width // 4, 3 * height // 8, 2 * width // 4, height // 8))
        text = pygame.font.SysFont('Comic Sans MS', height // 26).render('Выход', False, 'black')
        screen.blit(text, text.get_rect(center=(width // 2, 7 * height // 16)))
    pygame.display.flip()

if end:
    if score > scoreboard[9]:
        scoreboard[9] = score
        scoreboard.sort(reverse=True)
        file = open('scoreboard.txt', 'w')
        for line in scoreboard:
            file.write(f'{line}\n')
    open('save.txt', 'w').write('None')
else:
    methods.generate_shape(pool, shape, x, y, 'empty', turn)
    methods.save_save(pool, score)

pygame.quit()
