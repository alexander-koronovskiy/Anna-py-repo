def vector_v_complex(dv_massiv):
    complex_num = list()
    for i in range(len(dv_massiv)):
        complex_num.append(complex(dv_massiv[i][0], dv_massiv[i][1]))
    return complex_num


# a = [[1, 2], [3, 4], [5, 6]]
# b = vector_v_complex(a)

# ввод числа, преобразование типа в int
a = int(input())

# находит цифры числа
c = a % 10
b = a % 100 // 10
d = a // 100

# находит максимальную цифру числа
if(b > c):
    if (b > d):
        print(b)
if(c > b):
    if(c > d):
            print(c)
if(d > b):
    if (d > c):
        print(d)
if(c == b == d):
    print(c)
