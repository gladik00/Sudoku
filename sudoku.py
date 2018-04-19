
def take(): #дает список из 81 элемента
    a = open('sudoku.txt', 'r').read()
    p = a.split()
    for i in range(len(p)):
        p[i] = int(p[i])
    return p


def left(ex): #проверяет, остались ли 0
    q = 0
    for i in ex:
        if i == 0:
            q += 1
    if q == 0:
        return True
    else:
        return False


def check(ar, n): #проверяет, может ли в данной клетке быть такое значение, какое в ней стоит
    strings = []
    for i in range(9):
        strings.append([ar[9*i], ar[9*i + 1], ar[9*i + 2], ar[9*i + 3], ar[9*i + 4], ar[9*i + 5], ar[9*i + 6],
                        ar[9*i + 7], ar[9*i + 8]])
    check_string = 0
    for i in range(9):
        if ar[n] == strings[n // 9][i]:
            check_string += 1
    check_table = 0
    for i in range(9):
        if ar[n] == strings[i][n % 9]:
            check_table += 1
    check_square = 0
    square = []
    if n % 3 == 0:
        square.extend([ar[n], ar[n+1], ar[n+2]])
        n1 = n
        n2 = n + 1
        n3 = n + 2
    if n % 3 == 1:
        square.extend([ar[n], ar[n+1], ar[n-1]])
        n1 = n
        n2 = n + 1
        n3 = n - 1
    if n % 3 == 2:
        square.extend([ar[n], ar[n-1], ar[n-2]])
        n1 = n
        n2 = n - 1
        n3 = n - 2
    if (n // 9) % 3 == 0:
        square.extend([ar[n1 + 9], ar[n1 + 18], ar[n2 + 9], ar[n2 + 18], ar[n3 + 9], ar[n3 + 18]])
    if (n // 9) % 3 == 1:
        square.extend([ar[n1 + 9], ar[n1 - 9], ar[n2 + 9], ar[n2 - 9], ar[n3 + 9], ar[n3 - 9]])
    if (n // 9) % 3 == 2:
        square.extend([ar[n1 - 9], ar[n1 - 18], ar[n2 - 9], ar[n2 - 18], ar[n3 - 9], ar[n3 - 18]])
    for i in square:
        if ar[n] == i:
            check_square += 1
    if check_square == 1 and check_string == 1 and check_table == 1:
        return True
    else:
        return False


def first_null(ar): #выдает номер первого нуля
    q = 0
    for i in range(81):
        if ar[i] == 0:
            return i
            q = 1
            break
    if q == 0:
        return 'no'



def poss_list(ar, n):  #выдает список значений, которые могут быть в данной клетке массива
    poss = []
    for k in range(1, 10):
        copy = ar[:]
        copy[n] = k
        if check(copy, n):
            poss.append(k)
    return poss


def easy_try(ar): #считает простой судоку
    for k in range(81):
        for i in range(81):
            copy = ar[:]
            p_quantity = 0
            p_value = 0
            if ar[i] == 0:
                for j in range(9):
                    copy[i] = j + 1
                    if check(copy, i):
                        p_quantity += 1
                        p_value = copy[i]
            if p_quantity == 1:
                ar[i] = p_value
                break
        if left(ar):
            break
    return ar


def output(ar): #красиво оформляет вывод
    for i in range(9):
        if i % 3 == 0:
            print ('')
        print(ar[9 * i], ar[9 * i + 1], ar[9 * i + 2], '', ar[9 * i + 3], ar[9 * i + 4],
                ar[9 * i + 5], '', ar[9 * i + 6], ar[9 * i + 7], ar[9 * i + 8])


def diff_try(ar):
    k = first_null(ar)
    if k == 'no':
        return True
    else:
        poss = poss_list(ar, k)
        for i in poss:
            ar[k] = i
            if diff_try(ar):
                return True
            ar[k] = 0
        return False


almost_ready = easy_try(take())
ready = diff_try(almost_ready)
if ready:
    output(almost_ready)
print ('Danya sosunetz')
