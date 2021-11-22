

def read_array():
    n = int(input())
    arr = list(map(int, input().split()))
    return arr


def read_row():
    # Прочитали число на первой строке и привели к целому типу.
    a = int(input())
    # Сделали то же самое с числом на второй строке.
    b = int(input())
    return a, b
