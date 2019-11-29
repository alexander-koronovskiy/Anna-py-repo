
'''
# программа, вычисляющая часы и минуты
n=int(input())
m=int(input())
d=abs(n-m)//60
k=abs(n-m)%60
print(d,k)
'''

'''
# песец 
a=int(input())
print(a//2)
if (a//2):
    print("Четное число")
else:
    print("НЕЧетное число")
'''

'''
#максимальное число
a=int(input())
b=int(input())
if (a>b):
    print(a,"большее число")
else:
    print(b,"большее число")
'''

'''
# first wrong program in 1.6
first_num =input()
second_num =input()
third_num =input()
catalog = input()
if (first_num in catalog or second_num in catalog or third_num in catalog):
    print("YES")
else:
    print("NO")
'''
''' 
person = input()
status = "Ты не пройдешь!"
company = {"Арагорн", "Леголас", "Мериадок Брендибак", "Боромир", "Фродо Бэггинс"}
if (person in company):
    status = "Проходи!"
print(status)
'''

'''
if v > 0:
    v = v ** 2
else:
     v = v ** 4
if b > 0:
    b = b ** 2
else:
    b = b ** 4
if c > 0:
     c = c ** 2
else:
     c = c ** 4
'''
'''
# задача 1
v=int(input())
b=int(input())
c=int(input())
if v > 0:
    v = v ** 2
else:
     v = v ** 4
if b > 0:
    b = b ** 2
else:
    b = b ** 4
if c > 0:
     c = c ** 2
else:
     c = c ** 4
print(v, b, c)
'''

"""
#Задача 4 
a=int(input())
b=int(input())
c=a+b
if c<180:
    print("Треугольник существует")
    if (c==90):
        print("Прямоугольный треугольник")
    else:
        print("Не пряумогольный треугольник")
else:
    print("Нет такого треугольника")
"""

"""
# задача 2
a=int(input())
b=int(input())
c=int(input())
if a == b == c and a!=0 and b!=0 and c!==0:
    print("Равностороний треугольник")
else:
    print("Не равносторонний треугольник")
"""
''' 
# Задача 5
a=int(input())
b=a//100
c=a%100//10
d=a%10
h=b+c+d
l=h%2==0
print(l)
'''
"""
# Задача 6
a=int(input())
b=int(input())
c=int(input())
if a==b and a!=0 and b!=0 and c!=0 :
    print("Равнобедренный треугольник")
else:
   print ("Не равнобедренный треугольник")
"""
""" 
# Задача 3
a=int(input())
a1= a//10
a2=a%100//10
a3=a%100
b=a**2
c=a1+a2+a3
if (b==c):
    print("равен")
else:
    print("Не равен")
"""
