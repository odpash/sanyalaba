import math
import random


def generate_random_mtx(n, m):
    arr = []
    for i in range(n):
        arr.append(generate_random_arr(m))
    return arr


def generate_random_arr(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 1000))
    return arr


def lab1_task6_one(x, a):
    return (5 * math.sin(2 * math.pi * x) ** 2 - math.sqrt(math.fabs(x ** 4 - 2))) / 2 * math.atan(x) + 3.2 * 10 ** -2 * math.pi * x + math.log10(a)


def lab1_task6_two(x, y, z):
    return max(max(x * x, y * x), z * z) - min(x, y)


def lab1_task6_three(x, a):
    if x > a:
        return math.e ** (a * x) / 5
    elif x < a:
        return math.log(x * a, 2)
    else:
        return a * x ** 2


def lab1_task7_one(x, a, b):
    return (math.sqrt(3 * a ** 2 + 2 * b ** 2) * math.tan(a + b) ** 2) / math.sin(x) ** 2 + 10.52 * math.log(x, 2)


def lab1_task7_two(x, y, z):
    return min(x + y / 2 + z / 2.2 * x + 2 * y - z, x * y * z) ** 2 + 1


def lab1_task7_three(x):
    if x < -1:
        return 1 / x ** 2
    elif -1 <= x <= 2:
        return x * x
    elif x > 2:
        return 4


def lab2_task6_one(x):
    if x < -1:
        return x * math.cos(3 * x)
    elif -1 <= x <= 2:
        return 1.35
    else:
        return x ** math.sin(2 * x) ** 2


def lab2_task6_two(x):
    s = 0
    for i in range(5):
        s += (x ** 2 * math.factorial(i)) / ((i + 1) ** 2)
    return s


def lab2_task6_three(x):
    s = 0
    i = 4
    while True:
        i += 1
        last_s = s
        s += (x ** i) / ((1 + 5) ** (i + 1))
        if last_s == s:
            return round(s, 3)


def lab2_task7_one(x, a):
    if x > 7.5:
        return math.e ** (3 * x / a)
    elif 6.5 <= x <= 7.5:
        return math.log10(x)
    elif x < 6.5:
        return 2 ** x


def lab2_task7_two(n):
    s = 0
    for i in range(n):
        s += (2 + (1 / math.factorial(i))) ** 2
    return s


def lab2_task7_three():
    s = 0
    i = 4
    while True:
        i += 1
        last_s = s
        s += i / math.factorial(2 * i)
        if last_s == s:
            return round(s, 3)


def lab3_task6_one(n, arr):
    s = 1
    for i in range(n):
        s *= arr[i]
    return math.sqrt(math.fabs(s))


def lab3_task6_two(b):
    arr = []
    for i in range(1, b + 1):
        arr.append(1 / i)
    return arr


def lab3_task6_three(arr):
    sum1, count = 0, 0
    for i in range(len(arr)):
        if arr[i] < i ** 2:
            sum1 += arr[i]
            count += 1
    return sum1, count


def lab3_task6_four(n, m):
    mtx = [[0] * m] * n
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            mtx[i - 1][j - 1] = math.log10(i * i + j * j)
    return mtx


def lab3_task6_five(a):
    to_index = len(a)
    max_element = 0
    for i in range(len(a)):
        to_index -= 1
        for j in range(len(a)):
            if j >= to_index and a[i][j] > max_element:
                max_element = a[i][j]
    return max_element


def lab3_task7_one(n, arr):
    return 2 * sum(arr) ** 2


def lab3_task7_two(n):
    arr = []
    for i in range(n):
        arr.append(2 ** i + 3 ** (i + 1))


def lab3_task7_three(n, arr):
    sum1, count = 0, 0
    for i in arr:
        if i % 3 != 0:
            sum1 += i
            count += 1
    return sum1, count


def lab3_task7_four(n, m):
    mtx = [[0] * m] * n
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            mtx[i - 1][j - 1] = math.cos(1 / (i ** 2 + n * j))
    return mtx


def lab3_task7_five(mtx):
    max1 = 0
    to_minus = 0
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            ti = i
            if i > len(mtx) // 2:
                to_minus += 1
                ti = i - to_minus
            if (j <= ti or j >= len(mtx) - 1 - ti) and max1 < mtx[i][j]:
                max1 = mtx[i][j]
    return max1


print("Лабораторная работа №1")
print("Вариант 6")
print("Задание 1:", lab1_task6_one(0.2, 3))
print("Задание 2:", lab1_task6_two(2, 4, 3))
print("Задание 3:", lab1_task6_three(0.2, 3))
print("Вариант 7")
print("Задание 1:", lab1_task7_one(4, 1.7, 1.4))
print("Задание 2:", lab1_task7_two(4, 1.7, 1.4))
print("Задание 3:", lab1_task7_three(4))

print("Лабораторная работа №2")
print("Вариант 6")
print("Задание 1:", lab2_task6_one(0.2))
print("Задание 2:", lab2_task6_two(2))
print("Задание 3:", lab2_task6_three(3.5))
print("Вариант 7")
print("Задание 1:", lab2_task7_one(0.2, 4))
print("Задание 2:", lab2_task7_two(4))
print("Задание 3:", lab2_task7_three())


print("Лабораторная работа №3")
print("Вариант 6")
print("Задание 1:", lab3_task6_one(5, generate_random_arr(5)))
print("Задание 2:", lab3_task6_two(5))
print("Задание 3:", lab3_task6_three(generate_random_arr(5)))
print("Задание 4:", lab3_task6_four(5, 7))
print("Задание 5:", lab3_task6_five(generate_random_mtx(5, 5)))
print("Вариант 7")
print("Задание 1:", lab3_task7_one(5, generate_random_arr(5)))
print("Задание 2:", lab3_task7_two(5))
print("Задание 3:", lab3_task7_three(5, generate_random_arr(5)))
print("Задание 4:", lab3_task7_four(5, 7))
print("Задание 5:", lab3_task7_five(generate_random_mtx(5, 5)))
