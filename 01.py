# Создаем двумерный список с данными лабиринта
a = []
a.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
a.append([-1,  0, -1,  0,  0,  0, -1,  0,  0,  0, -1])
a.append([-1,  0,  0,  0, -1,  0, -1,  0, -1,  0, -1])
a.append([-1,  0, -1,  0, -1,  0,  0,  0, -1,  0, -1])
a.append([-1,  0, -1,  0, -1, -1, -1, -1, -1,  0, -1])
a.append([-1,  0, -1,  0,  0,  0,  0,  0, -1,  0, -1])
a.append([-1,  0, -1, -1, -1, -1, -1, -1, -1,  0, -1])
a.append([-1,  0,  0,  0,  0,  0,  0,  0, -1,  0, -1])
a.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])

# Метод вывода "красивого" лабиринта на экран
def printLab(a):
    # Перебираем список
    for i in a:
        for j in i:
            # Если элемент равен нулю, то выводим ЧЕТЫРЕ ПРОБЕЛА
            if j == 0:
                print("    ", end="")
            # Если -1, то выводим четыре звёздочки
            elif j == -1:
                print("****", end="")
            # Если число меньше 10, то добавляем в начале 0, то есть 01, 02, 03. Нужно для того,
            # чтобы не съехало форматирование лабиринта
            else:
                if j < 10:
                    print(f" 0{j} ", end="")
                else:
                    print(f" {j} ", end="")
        print()
    print()

# Метод поиска пути
def findPath(a, x, y, number):
    # Маркируем текущую (x, y) клетку
    a[x][y] = number

    # Если есть путь ВНИЗ
    if a[x + 1][y] == 0:
        # Вызываем этот же метод для клетки снизу (x + 1)
        findPath(a, x + 1, y, number + 1)
    # Если есть путь ВПРАВО
    if a[x][y + 1] == 0:
        # Вызываем этот же метод для клетки справа (y + 1)
        findPath(a, x, y + 1, number + 1)
    # Если есть путь ВЛЕВО
    if a[x][y - 1] == 0:
        findPath(a, x, y - 1, number + 1)
    # Если есть путь ВВЕРХ
    if a[x - 1][y] == 0:
        findPath(a, x - 1, y, number + 1)

print("До обработки: ")
printLab(a)
print()
findPath(a, 1, 1, 1)
print("После обработки")
printLab(a)



