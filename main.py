# функция уменьшает число до тех пор пока одно из них не станет нулем
# практически для этого используется цикл
def evklidsimply(a,b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b

#  функция расширенного евклида
# ax + by = gcd(a,b)
# алгоритм находит нод и его линейное представление

def evklid_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = evklid_extended(b % a, a)
    return (div, y - (b // a) * x, x)

# функция бинарного евклида
def binary_evklid(a,b):
    g = 1  # переменная для подсчета
    # согласно условиям и пунктам задачи мы все делаем
    # по пунктам
    while(a % 2 == 0 and b % 2 == 0):
        a = a/2
        b = b/2
        g = 2*g
    u,v = a,b
    while u != 0:
        if u % 2 == 0:
            u = u/2
        if v % 2 == 0:
            v = v/2
        if u >= v:
            u = u - v
        else:
            v = v - u
    d = g*v
    return d

# функция расширенного бинарного евклида
def evklid_binary_extended(a, b):
    g = 1 # переменная для подсчетов
    # выполняем все согласно алгоритму
    # объяснять даже не надо все по пунктам расписано в условии задачи
    while (a % 2 == 0 and b % 2 == 0):
        a = a / 2
        b = b / 2
        g = 2 * g
    u = a
    v = b
    A = 1
    B = 0
    C = 0
    D = 1
    while u != 0:
        if u % 2 == 0:
            u = u/2
            if A % 2 == 0 and B % 2 ==0:
                A = A/2
                B = B/2
            else:
                A = (A+b)/2
                B = (B-a)/2
        if v % 2 == 0:
            v = v / 2
            if C%2==0 and D%2==0:
                C = C/2
                D = D/2
            else:
                C = (C+b)/2
                D = (D-a)/2
        if u>=v:
            u = u - v
            A = A - C
            B = B - D
        else:
            v = v - u
            C = C - A
            D = D - B
    d = g*v
    x = C
    y = D
    return (d,x,y)

def main():
    # положим числа в переменные
    a = int(input("Введите числа a"))
    b = int(input("Введите число b"))
    if a >= 0 and 0 <= b <= a: # проверяем условия что все в порядке(согласно условиям задачи
        print("Вызываем функицю Евклида")
        print(evklidsimply(a,b)) # вызываем функцию простого евклида
        print("А теперь можно вызвать функцию расширенного")
        print(evklid_extended(a,b)) # вызываем функцию расширенного евклида
        print("А теперь функция бинарного Евклида")
        print(binary_evklid(a,b)) # вызываем функцию бинарного евклида
        print("А теперь функция расширенного бинарного Евклида")
        print(evklid_binary_extended(a,b)) # вызываем функцию расширенного бинарного евклида


if __name__ == '__main__':
    main()
