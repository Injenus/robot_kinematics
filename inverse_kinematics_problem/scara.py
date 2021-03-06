# Скара, 2 звена
import math

DECIMAL_PLACES = 2  # Количество знаков после запятой в обобщённых координатах.
A1_LENGTH = 0.4  # Длина первого звена.
A2_LENTGH = 0.8  # Длина второго звена.
ARM = 1  # Определяет ориентацию манипулятора: левая = -1, правая = 1.
DEFAULT_MODE = True  # Режим работы, True - с координатами по умолчанию.

default_coordinates = [[0.2, 0.4], [0.2, 0.6], [0.4, 0.8], [0.6, 0.8],
                       [0.8, 0.6], [0.5, 0.5], [0.8, 0.4], [0.6, 0.2],
                       [0.2, 0.4]]
delta_x = 0  # смещение по х для коррекции положения
delta_y = 0  # смещение по у для коррекции положения
for i in range(len(default_coordinates)):
    default_coordinates[i][0] += delta_x
    default_coordinates[i][1] += delta_y

class Coordinates():  # инициализация точки, сразу вычисляем обощённые координаты
    def __init__(self, name, x=0.0, y=0.0, z=0.0):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.calculaion_generalized_coordinates()

    # округление до digits-го знака
    def to_fixed(self, value, digits=2): return f"{value:.{digits}f}"

    # расчёт обобщённых координат для точки
    def calculaion_generalized_coordinates(self):
        a = math.atan(self.y / self.x)
        r = (self.x ** 2 + self.y ** 2) ** (1 / 2)
        g1 = math.acos(
            (A1_LENGTH ** 2 + r ** 2 - A2_LENTGH ** 2) / (2 * A1_LENGTH * r))
        g2 = math.asin((math.sin(g1) * A1_LENGTH) / (A2_LENTGH))
        self.q1 = (-math.pi) / 2 + a * ARM
        self.q2 = (g1 + g2) * ARM
        self.q3 = None
        self.q1 = self.to_fixed(self.q1, DECIMAL_PLACES)
        self.q2 = self.to_fixed(self.q2, DECIMAL_PLACES)

    def print_point(self):  # печатаем координаты точки
        print(
            '{}: x = {}, y = {}, z = {}'.format(self.name, self.x, self.y,
                                                self.z))

    def print_generalized_coordinates(self):  # вывод обощённых координат точки
        print(
            '{}: q1 = {}, q2 = {}, q3 = {}'.format(self.name, self.q1, self.q2,
                                                   self.q3))

point = []  # список полей класса Coordinates()
if not DEFAULT_MODE:
    num = 0  # количество точек
    input_text = 'Введите количество точек: '
    while True:  # требуем ввод натурального числа
        try:
            num = int(input(input_text))
        except ValueError:
            input_text = 'Вы ввели не натуральное число. Попробуйте снова: '
        else:
            if num < 1:
                input_text = 'Вы ввели не натуральное число. Попробуйте снова: '
            else:
                break

    for i in range(1,
                   num + 1):  # заполняем список точек полями класса Coordinates()
        if i != 3:  # ради падежа (люблю падежи)
            input_text = 'Введите координаты ' + str(
                i) + '-ой точки x, y через пробел: '
        else:
            input_text = 'Введите координаты ' + str(
                i) + '-eй точки x, y через пробел: '
        while True:
            try:
                x, y = map(float, input(input_text).split(' '))
            except ValueError:
                if i != 3:  # ради падежа (люблю падежи)
                    input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ой точки x, y через пробел: '
                else:
                    input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ей точки x, y через пробел: '
            else:
                break
        name = 'point_' + str(i)
        current_point = Coordinates(name, x, y)
        point.append(current_point)
else:
    for i in range(1, 1 + len(default_coordinates)):
        name = 'point_' + str(i)
        current_point = Coordinates(name, default_coordinates[i - 1][0],
                                    default_coordinates[i - 1][1])
        point.append(current_point)
print('\n', end='')
for i in range(len(default_coordinates)):
    point[i].print_generalized_coordinates()
