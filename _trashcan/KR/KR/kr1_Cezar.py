message = "ГРЬСШЯБЛ"
resMess = "ЩЛЦПЪУАК"
res = []
alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
key = 3

for key in range(1, 33):
    for i in range(len(message)):
        res.append(alfavit[(alfavit.find(message[i])-key)%len(alfavit)])
    print(key,"".join(res))
    res = []

for key in range(1, 33):
    for i in range(len(message)):
        res.append(alfavit[(alfavit.find(message[i])+key)%len(alfavit)])
    if ("".join(res) == resMess):
        print(key)
        
    res = []
