alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

x = "ТЯСЫЯОЦС"

res = ""
for i in range(len(x)):
    k = alf.find(x[i])+1
    res += alf[len(alf)-k]

print(res)