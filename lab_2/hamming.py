# ================== НАСТРОЙКИ ОКРУЖЕНИЯ ==================
# Импорт библиотек
import math


# ================== ОТОБРАЖЕНИЕ МАТРИЦ ==================

# Функция вывода данных ШИФРОВАНИЕ
def print_data_encode(original_sequence, checksum_vector, result_vector, checksum_matrix):
    print("Матрица контрольного суммирования:")
    print("  i  [*, *, 1, *, 2, 3, 4, *, 5, 6, 7, 8, 9]")
    print("  j  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]")

    c = 0
    for i in checksum_matrix:
        print(f"a[{c + 1}] {i}")
        c += 1

    print(f"  b  [_, _, {original_sequence[0]}, _, {original_sequence[1]}, {original_sequence[2]}, {original_sequence[3]}, _, {original_sequence[4]}, {original_sequence[5]}, {original_sequence[6]}, {original_sequence[7]}, {original_sequence[8]}]")
    print(f"beta [{checksum_vector[0]}, {checksum_vector[1]}, _, {checksum_vector[2]}, _, _, _, {checksum_vector[3]}, _, _, _, _, _]")
    print(f"b[t] {result_vector}")


# Функция заполнения матрицы контрольного суммирования TODO
def completed_checksum_matrix(checksum_matrix):
    for i in range(13):
        sequence_length = i + 1
        for j in range(4):
            checksum_matrix[j][i] = sequence_length % 2
            sequence_length //= 2

# Функция вывода данных РАСШИФРОВКА
def print_data_decode(checksum_vector, place_error):

    print(f"s[r] {checksum_vector}")
    if place_error != 0:
        print(f"Ошибка в {place_error} бите")
    else:
        print("Нет ошибок!")


# ##################### ШИФРОВАНИЕ #####################

# Функция кодирования бинарной последовательности данных
def encode():
    sequence_length = 9

    # Запись в массив. Преобразование элементов массива к типу int
    try:
        original_sequence = list(
            input(f"Введите последовательность длинной {sequence_length}: "))
        original_sequence = list(map(int, original_sequence))
    except:
        print("Ошибка в вводе данных!")
        exit(-1)

    # Заготовка для тестирования
    if original_sequence[0] == 1 and len(original_sequence) == 1:
        print("Использован шаблон: 101101010")
        original_sequence = [1, 0, 1, 1, 0, 1, 0, 1, 0]

    # Проверка на корректность последовательности
    for i in original_sequence:
        if (i != 0 and i != 1) or len(original_sequence) != sequence_length:
            print("Ошибка в вводе данных!")
            exit(-1)

    # Создание матрицы контрольного суммирования
    checksum_matrix = []
    for i in range(4):
        checksum_matrix.append([])
        for j in range(13):
            checksum_matrix[i].append(0)

    # Заполнить матрицу контрольного суммирования
    completed_checksum_matrix(checksum_matrix)

    # Добавляем места, куда потом вставим контрольные битов
    result_vector = []
    pos = 0
    for i in range(13):
        k = math.log2(i+1) % 1  # Вычисление степень двойки
        if k == 0:
            result_vector.append(0)
        else:
            # ВСТАВЛЯЕМ НУЛИ НА МЕСТО КУДА ПОДСТАВЯТСЯ ЧИСЛА
            result_vector.append(original_sequence[pos])
            pos += 1

    # Нахождение вектора контрольных сумм
    checksum_vector = []
    for i in range(4):
        summ = 0
        for j in range(13):
            summ += result_vector[j] * checksum_matrix[i][j]  # подсчёт единиц
        checksum_vector.append(summ % 2)  # чётность → 1 / 0

    # Получаем кодовое слово, вставляя контрольные биты
    pos = 0
    for i in range(13):
        if math.log2(i+1) % 1 == 0:  # подставляем в нужные места
            result_vector[i] = checksum_vector[pos]
            pos += 1

    print_data_encode(original_sequence, checksum_vector, result_vector, checksum_matrix)

# ##################### РАСШИФРОВКА #####################

# Функция декодирования бинарной последовательности данных
def decode():
    sequence_length = 13

    # Запись в массив. Преобразование элементов массива к типу int
    try:
        original_sequence = list(
            input(f"Введите последовательность длинной {sequence_length}: "))
        original_sequence = list(map(int, original_sequence))
    except:
        print("Ошибка в вводе данных!")
        exit(-1)

    # Заготовка для тестирования
    if original_sequence[0] == 2 and len(original_sequence) == 1:
        print("Использован шаблон: 0011111001010")
        original_sequence = [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0]

    # Проверка на корректность последовательности
    for i in original_sequence:
        if (i != 0 and i != 1) or len(original_sequence) != sequence_length:
            print("Ошибка в вводе данных!")
            exit(-1)

    # Преобразование списка к типу int
    original_sequence = list(map(int, original_sequence))

    # Создание двумерного списка
    checksum_matrix = []
    for i in range(4):
        checksum_matrix.append([])
        for j in range(13):
            checksum_matrix[i].append(0)

    # Получаем матрицу контрольного суммирования
    completed_checksum_matrix(checksum_matrix)

    # Нахождение вектора контрольных сумм
    checksum_vector = []
    for i in range(4):
        summ = 0
        for j in range(13):
            summ += original_sequence[j] * checksum_matrix[i][j]
        checksum_vector.append(summ % 2)

    place_error = 0

    # Сумма битых ячеек
    for i in range(4):
        place_error += checksum_vector[i] * 2**i

    print_data_decode(checksum_vector, place_error)

# ##################### ИНТЕРФЕЙС ПОЛЬЗОВАТЕЛЯ #####################


def main():
    while True:
        user_select = int(input("Выберите режим:\n" + "(1): Кодирование методом Хэмминга\n" +
                          "(2): Проверка методом Хэмминга\n" + "(3): Выход\n" + "Ваш выбор: "))

        if user_select == 1:
            encode()
        elif user_select == 2:
            decode()
        elif user_select == 3:
            exit(0)


if __name__ == "__main__":
    main()
