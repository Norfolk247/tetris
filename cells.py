class cell:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


class shape:
    def __init__(self, name, x, y, color, turn):
        self.name = name  # o i j l z t s
        self.x = x
        self.y = y
        self.color = color
        self.turn = turn  # 0 1 2 3

    def shape(self):
        if self.name == 'o':
            return [(self.x, self.y), (self.x + 1, self.y),
                    (self.x, self.y - 1), (self.x + 1, self.y - 1)]
        if self.turn == 0:
            if self.name == 'i':
                return [(self.x, self.y + 1),
                        (self.x, self.y),
                        (self.x, self.y - 1),
                        (self.x, self.y - 2)]
            if self.name == 'j':
                return [(self.x, self.y + 1),
                        (self.x, self.y),
                        (self.x - 1, self.y - 1), (self.x, self.y - 1)]
            if self.name == 'l':
                return [(self.x, self.y + 1),
                        (self.x, self.y),
                        (self.x, self.y - 1), (self.x + 1, self.y - 1)]
            if self.name == 'z':
                return [(self.x - 1, self.y), (self.x, self.y),
                        (self.x, self.y - 1), (self.x + 1, self.y - 1)]
            if self.name == 't':
                return [(self.x, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y)]
            if self.name == 's':
                return [(self.x, self.y), (self.x + 1, self.y),
                        (self.x - 1, self.y - 1), (self.x, self.y - 1)]
        if self.turn == 1:
            if self.name == 'i':
                return [(self.x - 2, self.y), (self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y)]
            if self.name == 'j':
                return [(self.x - 1, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y)]
            if self.name == 'l':
                return [(self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y),
                        (self.x - 1, self.y - 1)]
            if self.name == 'z':
                return [(self.x, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y),
                        (self.x - 1, self.y - 1)]
            if self.name == 't':
                return [(self.x, self.y + 1),
                        (self.x, self.y), (self.x + 1, self.y),
                        (self.x, self.y - 1)]
            if self.name == 's':
                return [(self.x - 1, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y),
                        (self.x, self.y - 1)]
        if self.turn == 2:
            if self.name == 'i':
                return [(self.x, self.y + 1),
                        (self.x, self.y),
                        (self.x, self.y - 1),
                        (self.x, self.y - 2)]
            if self.name == 'j':
                return [(self.x, self.y + 1), (self.x + 1, self.y + 1),
                        (self.x, self.y),
                        (self.x, self.y - 1)]
            if self.name == 'l':
                return [(self.x - 1, self.y + 1), (self.x, self.y + 1),
                        (self.x, self.y),
                        (self.x, self.y - 1)]
            if self.name == 'z':
                return [(self.x - 1, self.y), (self.x, self.y),
                        (self.x, self.y - 1), (self.x + 1, self.y - 1)]
            if self.name == 't':
                return [(self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y),
                        (self.x, self.y - 1)]
            if self.name == 's':
                return [(self.x, self.y), (self.x + 1, self.y),
                        (self.x - 1, self.y - 1), (self.x, self.y - 1)]
        if self.turn == 3:
            if self.name == 'i':
                return [(self.x - 2, self.y), (self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y)]
            if self.name == 'j':
                return [(self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y),
                        (self.x + 1, self.y - 1)]
            if self.name == 'l':
                return [(self.x + 1, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y)]
            if self.name == 'z':
                return [(self.x, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y),
                        (self.x - 1, self.y - 1)]
            if self.name == 't':
                return [(self.x, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y),
                        (self.x, self.y - 1)]
            if self.name == 's':
                return [(self.x - 1, self.y + 1),
                        (self.x - 1, self.y), (self.x, self.y),
                        (self.x, self.y - 1)]
