def ColumnToRow(lis):
    row = []
    for x in lis:
        row.append(x[0])
    return row


def Decrypt(rowKeys, columnKeys, Cipher, dic):
    items = sum(sum(1 for i in row if i) for row in Cipher)

    cols, rows = len(columnKeys)+1, int(items/len(columnKeys))+1

    array2d = [[0 for x in range(cols)] for y in range(rows)]
    array2d[0] = [0] + columnKeys

    j = 0
    for i in range(1, rows):
        array2d[i][0] = rowKeys[j]
        j += 1
        if j >= len(rowKeys):
            j = 0

    temp = ColumnToRow(array2d)

    for i in range(len(dic)):
        colIndex = array2d[0].index(dic[i][2])

        indices = [m for m, x in enumerate(temp) if x == dic[i][1]]
        rowIndex = indices[dic[i][3]-1]

        array2d[rowIndex][colIndex] = dic[i][0]

    for row in array2d:
        print(row)

    decrypted = ''
    for i in range(1, rows):
        for j in range(1, cols):
            decrypted += array2d[i][j]

    return decrypted


def Encrypt(Matrix, numberofCols, numberOfBlocks):
    Blocks = [[] for i in range(numberOfBlocks)]

    for i in range(1, ROWS):
        for j in range(1, COLS):
            colKey = Matrix[0][j]
            rowKey = Matrix[i][0]
            block = defineBlock(rowKey, colKey, numberofCols)
            Blocks[block-1].append(Matrix[i][j])
    return Blocks


def defineBlock(r, c, n):
    k = (r-1)*n + c
    return k


def defineSection(i, division):
    return (i//division + 1)

 # ————————————————————————————————————————————————————————————————————————————————————————————————

# Способ шифрования
message = "МЕТОДяРАССЕЧЕНИЯ-РАЗНЕСЕНИЯ."
columnKeys = [3, 2, 4, 1]
rowKeys = [3, 1, 2]

# Информация о шифре
strlength = len(message)
blocksNumber = 12
ColKeysNumber = 4
RowKeysNumber = int(blocksNumber/ColKeysNumber)
COLS = ColKeysNumber+1
ROWS = int(strlength//ColKeysNumber)+1

# Создание нулевой матрицы:
Matrix = [[0 for x in range(ColKeysNumber+1)] for y in range(ROWS)]
Matrix[0] = [0] + columnKeys

# Добавление ключей строк:
j = 0
for i in range(1, ROWS):
    Matrix[i][0] = rowKeys[j]

    j += 1
    if j >= len(rowKeys):
        j = 0

# Вывод информации о шифре
print('\n' + "Исходное сообщение:", message)
print("Длина сообщения:", strlength)
print("Ключи столбцов:", columnKeys)
print("Клавиши строк:", rowKeys)
print("Количество блоков:", blocksNumber)
print()

# Заполнение матрицы буквами и создание списка расшифровок:
dic = []
m = 0
for i in range(1, ROWS):
    for j in range(1, COLS):
        Matrix[i][j] = message[m]
        cKey = Matrix[0][j]
        rKey = Matrix[i][0]
        section = defineSection(i-1, RowKeysNumber)
        dic.append([message[m], rKey, cKey, section])
        m += 1


print("Сообщение, распределенное по определенным строкам и столбцам:")
for row in Matrix:
    print(row)
print()

# Распределение сообщения по блокам на основе ключей столбцов и строк:
Cipher = Encrypt(Matrix, ColKeysNumber, blocksNumber)

print("Результат шифрования (блоки):")
i = 1
for bl in Cipher:
    print("Номер блока " + str(i) + ":", bl)
    i += 1

print('\n' + "Расшифрованная структура таблицы:")
decrypted = Decrypt(rowKeys, columnKeys, Cipher, dic)

print('\n' + "Окончательное расшифрованное сообщение:" + '\n', decrypted, '\n')
