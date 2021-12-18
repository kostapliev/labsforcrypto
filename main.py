from math import gcd


def f(x, n):
    return (x*x+5)%n

def fu(n,a, b, d):
    a = f(a, n) % n
    b = f(f(b, n), n) %n
    d = gcd(a-b, n)
    if 1<d<n:
        p = d
        print(p)
        exit()
    if d == n:
        print("Не найдено")
    if d == 1:
        global ag
        ag = b
        fu(n, a, b, d)


def main():
    n = 1359331
    c = 1
    a = c
    b = c
    a = f(a, n) % n
    b = f(a,n) % n
    d = gcd(a-b, n)
    if 1<d<n:
        p = d
        print(p)
        exit()
    if d == n:
        pass
    if d == 1:
        fu(n, a, b, d)


main()