import sys # импортируем sys

def prrint(lists): # функция для красивой печати матриц
    for i in lists:
        for j in i:
            print(j, end=" ")
        print()


def marhsrutshifr(): # задание 1. Маршрутное шифрование.
    text = input("Input anything").replace(' ', '') # вводим текст и очищаем от пробелов
    n = int(input("Введите число n")) # на сколько блоков надо разбить текст
    m = int(input("Введите число m")) # на сколько блоков надо разбить текст
    parol = input("Введите слово-пароль") # слово-пароль
    # мы не предусмотрели проверку на соотвествие
    lists = [['a' for i in range(0, n)] for j in range(m)] #создаем матрицу nxm
    it = 0 #итератор
    for i in range(m):
        for j in range(n):
            if it < len(text):
                lists[i][j] = text[it] #заполняем текстом
                it += 1
    lis = list()
    for i in range(n):
        lis.append(parol[i]) # добавляем пароль в список
    lists.append(lis) # а список в матрицу
    prrint(lists)
    result = "" # сюда будем записывать результат
    spisok = sorted(lists[len(lists) - 1]) # сортируем по буквам пароль
    for i in spisok: # и согласно сортировке выписывает столбцами результат
        print(i, " = ", lists[len(lists)-1].index(i))
        for j in range(len(lists)):
            if j==len(lists)-1:
                continue
            result += lists[j][lists[len(lists)-1].index(i)]
    print(result)


# функция для поворота матрицы. нужен для 2рого задания
def rot90(matrix):
    return[list(reversed(col)) for col in zip(*matrix)]

# функция удаления чисел из матрицы нужен для 2 рого задания
def udalenie(largelist, inn, k):
    for i in range(k * 2):
        for j in range(k * 2):
            if largelist[i][j] == inn:
                largelist[i][j] = " "
                return


def cardangrille(): # второе задания
    k = int(input("Введите число k")) # вводим наше число  k
    s=1
    lists = [[i for i in range(k)] for i in range(k)] # строим матрицу этого размера
    for i in range(k):
        for j in range(k):
            lists[i][j] = s # заполняем матрицу числами
            s += 1
    print(lists)
    lists1 = rot90(lists) # заранее делаем повороты и сохраняем эти матрицы, чтоб потом приклеить друг к другу
    lists2 = rot90(lists1)
    lists3 = rot90(lists2)
    largelist = [[1 for i in range(2*k)] for i in range(2*k)] # создаем большую матрицу, сюда будем клеить
    for i in range(k):  # тут уже каждый цикл клеет все: 1 верхний кубик, 2 правый верхний кубик и тд
        for j in range(k):
            largelist[i][j] = lists[i][j]
    i1 = 0
    j1 = 0
    for i in range(0, k):
        for j in range(k, k*2):
            largelist[i][j] = lists1[i1][j1]
            j1 += 1
        j1 = 0
        i1 += 1
    i1 = 0
    j1 = 0
    for i in range(k, k*2):
        for j in range(k, k * 2):
            largelist[i][j] = lists2[i1][j1]
            j1 += 1
        j1 = 0
        i1 += 1
    i1 = 0
    j1 = 0
    for i in range(k, k * 2):
        for j in range(0, k):
            largelist[i][j] = lists3[i1][j1]
            j1 += 1
        j1 = 0
        i1 += 1
    prrint(largelist)
    text = "договорподписали" # текст который мы шифруем. его можно менять и даже нужно
    largelist_a = [[" " for i in range(2*k)] for i in range(2*k)] # тут вторая матрица из букв. Сюда будем вписывать буквы
    s = 0
    li = [i for i in range(1,k**2+1)] #список из чисел, которые надо удалить
    for inn in li:
        udalenie(largelist, inn, k) # удаляем по очереди. Да, согласен алгоритм удаления такое себе))
    ind = 0
    # а тут уже "выписываем" буквы. Если текста еще есть то делаем повороты и тд
    for i in range(k * 2):
        for j in range(k * 2):
            if largelist[i][j] == largelist_a[i][j] and len(text) > 0:
                largelist_a[i][j] = text[0]
                text = text[1:]
    largelist = rot90(largelist)
    for i in range(k * 2):
        for j in range(k * 2):
            if largelist[i][j] == largelist_a[i][j] and len(text) > 0:
                largelist_a[i][j] = text[0]
                text = text[1:]
    if len(text) > 0:
        largelist = rot90(largelist)
        for i in range(k * 2):
            for j in range(k * 2):
                if largelist[i][j] == largelist_a[i][j] and len(text) > 0:
                    largelist_a[i][j] = text[0]
                    text = text[1:]
    if len(text) > 0:
        largelist = rot90(largelist)
        for i in range(k * 2):
            for j in range(k * 2):
                if largelist[i][j] == largelist_a[i][j] and len(text) > 0:
                    largelist_a[i][j] = text[0]
                    text = text[1:]
    prrint(largelist_a)
    stri = input("Введите пароль")
    # тут дописываем пароль или удаляем чтоб длина слова была норм и потом прибавляем к матрице
    if len(stri) > k*2:
        stri = stri[:k*2]
    elif len(stri) < k*2:
        while len(stri) != k*2:
            stri += "z"
    largelist_a.append(list(stri))
    prrint(largelist_a)
    result = ""
    #фактически эта часть кода, такая же как в первом задании.
    spisok = sorted(largelist_a[len(largelist_a) - 1])
    for i in spisok:
        print(i, " = ", largelist_a[len(largelist_a) - 1].index(i))
        for j in range(len(largelist_a)):
            if j==len(largelist_a)-1:
                continue
            result += largelist_a[j][largelist_a[len(largelist_a) - 1].index(i)]
    print(result.replace(" ", ""))

# Вижинер
# слил из хабра. там есть все объяснение: дублировать, думаю, не стоит: https://habr.com/ru/post/140820/
def form_dict():
    d = {}
    iter = 0
    for i in range(0,127):
        d[iter] = chr(i)
        iter = iter +1
    return d

def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict()

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value)
    return list_code

def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0
    return dic


def full_encode(value, key):
    dic = comparator(value, key)
    print('Compare full encode', dic)
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go)
    return lis


def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict()

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value])
    return list_code

def full_decode(value, key):
    dic = comparator(value, key)
    print('Deshifre=', dic)
    d = form_dict()
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go)
    return lis

def vijer():
    word = "salamualeikum"
    key = "password"
    sys.stdout.write(word)
    sys.stdout.write(key)
    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
    sys.stdout.write(str(key_encoded))
    sys.stdout.write(str(value_encoded))
    shifre = full_encode(value_encoded, key_encoded)
    print('Шифр=', ''.join(decode_val(shifre)))

    decoded = full_decode(shifre, key_encoded)
    print('Decode list=', decoded)
    decode_word_list = decode_val(decoded)
    print('Word=', ''.join(decode_word_list))

def main():
    command = int(input("Введите команду для продолжения 1: первое задание, 2: второе задание, 3:третье задание"))
    if command==1:
        marhsrutshifr()
    elif command==2:
        cardangrille()
    elif command==3:
        vijer()
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
