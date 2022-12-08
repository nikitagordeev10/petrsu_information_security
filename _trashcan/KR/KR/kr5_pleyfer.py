text = "ПАССИВНЫЕ_УГРОЗЫ"
text = [x for x in text]
res = ''
m = [
    ["П","А","Т","И","С","О"],
    ["Н","Б","В","Г","Д","Е"],
    ["Ё","Ж","З","Й","К","Л"],
    ["М","Р","У","Ф","Х","Ц"],
    ["Ч","Ш","Щ","Ъ","Ы","Ь"],
    ["Э","Ю","Я","_",".",","],
    ]

simvol = "Ъ"
for i in range(1,len(text),2):
    if text[i] == text[i-1]:
        text.insert(i,simvol)
if len(text)%2 != 0:
    text.append(simvol)

print(text)
res = ""
for i in range(0, len(text), 2):# Берём по два аргумента
    # Ищем кооржинаты строк и столбоц символа
    flag = False
    for j in range(6):
        for k in range(6):
            if m[j][k] == text[i]:
                x1 = j
                y1 = k
                flag = True
                break
        if flag:
            break

    flag = False
    for j in range(6):
        for k in range(6):
            if m[j][k] == text[i+1]:
                x2 = j
                y2 = k
                flag = True
                break
        if flag:
            break
    # print(x1,y1,x2,y2)

    # Если в одной строке, то справа в столбце
    if (x1 == x2):
        y1 = (y1 + 1) % 6 
        y2 = (y2 + 1) % 6
        res += m[x1][y1] + m[x2][x2]
        continue
    # Если в одном столбце, то снизу в строке
    if (y1 == y2):
        x1 = (x1 + 1) % 6 
        x2 = (x2 + 1) % 6
        res += m[x1][y1] + m[x2][y2]
        continue
        
    # Иначе ищем углы
    if ((y1 > y2) and (x1 < x2)) or ((y1 < y2) and (x1 > x2)):
        res += m[x2][y1] + m[x1][y2]
    else:
        res += m[x1][y2] + m[x2][y1]

# encode Шифрует верно, если матрицу вручную заполнить правильно
print(res)


#######
text = "ЭФЛБХВПБАЦЕБЕИ,ИЕАНЦПБИГГМЦАПРФОЛГ"
text = [x for x in text]
res = ''
m = [
    ["П","А","Т","И","С","О"],
    ["Н","Б","В","Г","Д","Е"],
    ["Ё","Ж","З","Й","К","Л"],
    ["М","Р","У","Ф","Х","Ц"],
    ["Ч","Ш","Щ","Ъ","Ы","Ь"],
    ["Э","Ю","Я","_",".",","],
    ]

simvol = "Ъ"
for i in range(1,len(text),2):
    if text[i] == text[i-1]:
        text.insert(i,simvol)
if len(text)%2 != 0:
    text.append(simvol)

print(text)
res = ""
for i in range(0, len(text), 2):# Берём по два аргумента
    # Ищем кооржинаты строк и столбоц символа
    flag = False
    for j in range(6):
        for k in range(6):
            if m[j][k] == text[i]:
                x1 = j
                y1 = k
                flag = True
                break
        if flag:
            break

    flag = False
    for j in range(6):
        for k in range(6):
            if m[j][k] == text[i+1]:
                x2 = j
                y2 = k
                flag = True
                break
        if flag:
            break
    # print(x1,y1,x2,y2)

    # Если в одной строке, то справа в столбце
    if (x1 == x2):
        y1 = (y1 - 1) % 6 
        y2 = (y2 - 1) % 6
        res += m[x1][y1] + m[x2][x2]
        continue
    # Если в одном столбце, то снизу в строке
    if (y1 == y2):
        x1 = (x1 - 1) % 6 
        x2 = (x2 - 1) % 6
        res += m[x1][y1] + m[x2][y2]
        continue
        
    # Иначе ищем углы
    if ((y1 > y2) and (x1 < x2)) or ((y1 < y2) and (x1 > x2)):
        res += m[x1][y2] + m[x2][y1]
    else:
        res += m[x2][y1] + m[x1][y2]

# decode Шифрует верно, если матрицу вручную заполнить правильно. Откидываем вручную ненужный символ
print(res)