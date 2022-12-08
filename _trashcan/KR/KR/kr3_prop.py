alf = {
    'А': [0, 123, 231, 321, 213],
    'Б': [0, 456, 564],
    'В': [0, 789, 897],
    'Г': [0, 234, 342],
    'Д': [0, 876, 768],
    'Е': [0, 345, 453, 543, 435],
    'Ё': [0, 567, 675, 765],
    'Ж': [0, 976, 769],
    'З': [0, 134, 341],
    'И': [0, 965, 659, 569],
    'Й': [0, 145, 451],
    'К': [0, 954, 549, 459],
    'Л': [0, 156, 561, 651],
    'М': [0, 943, 439, 349],
    'Н': [0, 167, 671, 761, 617],
    'О': [0, 932, 329, 239, 392, 923],
    'П': [0, 178, 781, 871],
    'Р': [0, 912, 129, 219],
    'С': [0, 189, 891, 981, 819],
    'Т': [0, 975, 759, 579, 795],
    'У': [0, 135, 351],
    'Ф': [0, 964],
    'Х': [0, 146, 461],
    'Ц': [0, 953],
    'Ч': [0, 157, 571],
    'Ш': [0, 942, 429],
    'Щ': [0, 168, 681],
    'Ъ': [0, 931],
    'Ы': [0, 179],
    'Ь': [0, 952],
    'Э': [0, 158, 581],
    'Ю': [0, 941, 419],
    'Я': [0, 169, 691, 961],
    '_': [0, 930, 309, '039', 390, 903, '093'],
}

x = 'ГРИФ_СЕКРЕТНОСТИ'
res = ""
for i in x:
    alf[i][0] += 1
    n = alf[i][alf[i][0]]
    res += str(n)

print(res)

x = '189965891975345943167932453930178912329234129123439349671239543309392456435981781345157453761659543'
for i in range(0, len(x), 3):
    print(x[i]+x[i+1]+x[i+2])