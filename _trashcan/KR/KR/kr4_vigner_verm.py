alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"


# Вижинер
key = "ЩАВЕЛЬ"
x = "УРОВЕНЬ_ЗАЩИЩЁННОСТИ"

# Создаем таблицу
a = []
for i in range(len(alf)):
    a.append([])
    for j in range(len(alf)):
        n = (j + i) % len(alf)
        a[i].append(alf[n])
# encode
res = ""
for i in range(len(x)):
    y1 = a[0].index(x[i])
    y2 = a[0].index(key[i % len(key)]) 

    res += a[y1][y2]

print(res)

# decode
x = "ГЙГЬТЕЦЦГТСКДУФЮОЯ_Н"
key = "ЧЕСНОК"

res = ""
for i in range(len(x)):
    y2 = a[0].index(key[i % len(key)]) 
    y1 = a[y2].index(x[i])

    res += a[0][y1]

print(res)

# Вернам
alf = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
alf_num = []
for i in range(len(alf)):
    alf_num.append(bin(i)[2:].zfill(5))

x = "ВДНЗМИ_ГВСДЦЖГНКУЪД"
key = "ВИНОГРАД"

result = ""
# encode and decode
for i in range(len(x)):
    word = alf_num[alf.index(x[i])]
    key_num = alf_num[alf.index(key[i % len(key)])]
    res = ""

    # Исключающие или
    for i in range(len(word)):
        res += str(int(word[i]) ^ int(key_num[i]))
    
    n = alf_num.index(res)
    result += alf[n]

print(result)
    
