import random

# тест ферма где n число которое проверяется
# а test_count это количество прогонов
def ferma(n, test_count):
    for i in range(test_count):

        a = random.randint(2, n - 1)

        if (a ** (n - 1) % n != 1):
            print("Составное")
            return False
    print("Простое")
    return True



# функция для бинарного эксп
def modulo(base, exponent, mod):
    x = 1
    y = base
    while (exponent > 0):
        if (exponent % 2 == 1):
            x = (x * y) % mod

        y = (y * y) % mod
        exponent = exponent // 2

    return x % mod


# нахождение символа якоби
# алгоритм в принципе расписан в лабе

def calculateJacobian(a, n):
    if (a == 0):
        return 0  # (0/n) = 0

    ans = 1
    if (a < 0):

        # (a/n) = (-a/n)*(-1/n)
        a = -a
        if (n % 4 == 3):
            # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans

    if (a == 1):
        return ans  # (1/n) = 1

    while (a):
        if (a < 0):

            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if (n % 4 == 3):
                # (-1/n) = -1 if n = 3 (mod 4)
                ans = -ans

        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans

        # меняем местами
        a, n = n, a

        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n

        if (a > n // 2):
            a = a - n

    if (n == 1):
        return ans

    return 0


# тест соловея штрассена, для получения более-менее правильного результата,
# нужно прогнать его много раз,

def solovoyStrassen(p, iterations):
    if (p < 2):
        return False
    if (p != 2 and p % 2 == 0):
        return False

    for i in range(iterations):

        # генерация рандомного числа  a
        a = random.randrange(p - 1) + 1
        jacobian = (p + calculateJacobian(a, p)) % p
        mod = modulo(a, (p - 1) / 2, p)

        if (jacobian == 0 or mod != jacobian):
            return False

    return True

# Алгоритм Миллера Рабина
# true = значит простое
# false = значит составное
def miller_rabin(n):
    if n != int(n):
        print("не простое!")
        return False
    n = int(n)
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        print("не простое!")
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        print("простое!")
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            print("не простое!")
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                print("не простое!")
                return False
        print("простое!")
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            print("не простое!")
            return False
    print("простое!")
    return True


def main():
    n = int(input("Введите число для ферма"))
    print("Тест ферма для числа ", n )
    ferma(n, 500)
    print("Тест миллера рабина")
    n = int(input("Введите число для миллера рабина"))
    miller_rabin(n)
    n = int(input("Введите число для соловея штрассена"))
    if (solovoyStrassen(n, 500)):
        print(n, "простое число ");
    else:
        print(n, "составное число");


if __name__ == '__main__':
    main()
