# ##################### НАСТРОЙКИ ОКРУЖЕНИЯ #####################
import struct
import time
import math
from datetime import datetime
import matplotlib.pyplot as plt

# ##################### ГЕНЕРАТОР ПСЕВДОСЛУЧАЙНЫХ ЧИСЕЛ #####################

# Текущая микросекунда


def microsecond():
    return datetime.now().microsecond

# Текущий час


def hour():
    return datetime.now().hour

# Текущий день


def day():
    return datetime.now().day

# Текущий месяц


def month():
    return datetime.now().month

# Текущий год


def year():
    return datetime.now().year

# Получение случайных a и b и с


def generate_abc():
    n = 24
    m = 2 ** n

    # Параметр a. От времени суток, остаток.
    a = math.ceil(microsecond() / math.ceil(math.sqrt(day() / 57))) + \
        math.ceil(day() / math.ceil(year() * month())) + \
        math.ceil(34 / (7 + microsecond() % 24)) - year() * month()
    while a % 6 != 1:
        a += 1

    # Параметр b. От времени суток, остаток, НОД.
    b = year() * month() + 5 * \
        math.ceil(microsecond() / 104) + \
        math.ceil(31 / (12 + microsecond() % 14)) - year() * month()
    while b % 2 != 1 and math.gcd(b, m) != 1:
        b += 1

    # Параметр c. От времени суток.
    c = math.ceil(microsecond() / hour()) + math.ceil(year() * hour()) + \
        math.ceil(math.sqrt(day() / 43)) + \
        math.ceil(71 / (22 + microsecond() % 24)) + year() * month()

    # Вывод значений
    print("Значения параметров:", "\na =", a, "\nb =", b, "\nc =", c)

    return a, b, c, m, n


# ГПСЧ. Возвращает список или одно число. ci = (a*ci-1+ b) (mod m)
def linear_congruent_generator(a, b, c, m, n, sequence_length):

    # degree_of_two = (microsecond() + day()) % 24
    degree_of_two = n

    # Последовательность длины 1 (ограничение сверху 4096)
    if sequence_length == 1:
        return [math.ceil((a * c + b) % 2**degree_of_two) % 4096]

    # Последовательность длины sequence_length (ограничение сверху 4096)
    sequence_result = [0 for i in range(sequence_length + 1)]
    sequence_result[0] = math.ceil(c)

    for i in range(1, sequence_length + 1):
        sequence_result[i] = math.ceil(
            (a * sequence_result[i-1] + b) % 2**degree_of_two) % 4096

    return sequence_result[1:sequence_length + 1]

# ##################### ШИФРОВАНИЕ #####################

# Вывод гистограммы


def encrypt(text):
    path_to_file = input(
        "Введите путь, куда сохранить зашифрованное сообщение (формат .txt): ")
    result_message = open(path_to_file, 'w', encoding="utf-8")
    s = ""

    # Читаем ключ
    path_to_key = input("Введите путь до файла для ключа (формат .key): ")
    f = open(path_to_key, 'r', encoding="utf-8")
    key_from_file = f.read()
    f.close()

    a, b, c = key_from_file.split(" ")

    key = linear_congruent_generator(len(text), int(a), int(b), int(c))

    # starting time
    start = time.time()

    # Гаммирование
    for i in range(len(text)):
        simvol = ord(text[i]) ^ int(key[i])
        s += chr(simvol)

    # end time
    end = time.time()
    print("Execution time of the program is - ", end-start)

    result_message.write(s)
    result_message.close()


# ##################### ИНТЕРФЕЙС ПОЛЬЗОВАТЕЛЯ #####################

def main():

    text = None
    key = None

    while True:
        user_select = int(input("Выберите режим:\n" + "(1): Сгенерировать и записать в файл ключ\n" + "(2): Зашифровать файл\n" + "(3): Дешифровать файл\n" + "(4): Выход\n" + "Ваш выбор: "))

        # Сгенирировать параметры a, b, c
        if user_select == 1:
            a, b, c, m, n = generate_abc()

        # Сгенирировать параметры a, b, c
        if user_select == 1:
            a, b, c, m, n = generate_abc()

        # Сгенерировать и вывести последовательность в консоль
        elif user_select == 2:
            try:
                sequence_length = int(
                    input("Введите размер последовательности: "))
                data = linear_congruent_generator(
                    a, b, c, m, n, sequence_length)
                print("a = %d\n" % (a) + "b = %d\n" % (b) + "c = %d" % (c))
                print("Generated sequence:", data)
            except:
                print("В начале необходимо сгенирировать параметры a, b, c!")

        # Сгенерировать и записать последовательность в файл. Вывести гистограмму
        elif user_select == 3:
            try:
                # Генерация данных
                sequence_length = int(
                    input("Введите размер последовательности: "))
                data = linear_congruent_generator(
                    a, b, c, m, n, sequence_length)
                # Запись в последовательности в файл
                f = open('output.txt', 'w')
                f.write("a = %d\n" % (a) + "b = %d\n" % (b) + "c = %d\n" % (c) +
                        "Generated sequence: ")
                for item in data:
                    f.write("%s " % str(item))
                f.close()
                # Печать гистограммы на экран
                print_histogram(data)
            except:
                print("В начале необходимо сгенирировать параметры a, b, c!")

        # Выход
        elif user_select == 4:
            exit(0)


# ##################### ЗАПУСК ПРОГРАММЫ #####################

if __name__ == "__main__":
    main()
