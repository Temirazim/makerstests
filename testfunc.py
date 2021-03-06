
#№1
#   // Находим минимальное положительное целое число, которого нет в списке. 
# Если список содержит только отрицательные числа, верните 1. 
# Все элементы являются целыми числами:
# Пример: [1,2,3,4,6] - Ответ 5
# Пример: [1,2,3] - Ответ 4
# Пример: [-1, -2, -6] - Ответ 1

# def min(cop):
#     b =5
#     for i in cop:
#         if b not in cop:
#             print(b)
#             break
# min([1,2,3,4,6])    


# def lop(top):
#     b = 4
#     for i in top:
#         if b not in top:
#             print(b) 
#             break
# lop([1,2,3])

# def pot(cat):
#     c = 1
#     for i in cat:
#         if c not in cat:
#             print(c)
#             break
# pot([-1, -2, -6])        

#№2
# Попросить пользователя ввести текст. В результате вывести процент букв 
# в верхнем регистре (заглавные) и в нижнем регистре (прописные).

# def myfunc():
#     text = input("Введите текст: ")
#     upper_ = 0
#     lower_ = 0
#     for i in text:
#         if i.isupper():
#             upper_ += 1
#         else:
#             lower_ += 1
#     result = upper_ + lower_
#     b = (upper_ / result) * 100
#     c = (lower_ / result) * 100
#     print(round(b, 2), "%", "Upper")
#     print(round(c, 2), "%", "lower")
# myfunc()




# "Аналог шифра цезаря ". Программа должна запрашивать элементы списка через пробел. 
# После чего пользователь должен ввести значение для сдвига элементов списка. 
# Значение может быть как положительным, так и отрицательным. Если значение положительное, 
# элементы списка должны сдвигаться вправо, если отрицательное - влево. Результат необходимо вывести на экран:
# Введенные данные: [5,7,9,10,2], 2
#  Результат:        [9,10,2,5,7]
# """
#метод Тимура
# spis = input('Input numbers:').split()
# b = []
# for i in spis:
#     b.append(int(i))
# com = int(input('Moving :'))
# print("Before-"+str(b)+', '+str(com))
# if com > 0:
#     b = b[com:]+b[:com]#Старт,стоп,шаг:СРЕЗЫ используется:list,str,tuple
#     print("After-",b)
# elif com < 0:
#     b = b[com:]+b[:com:]
#     print("After-",b)


#№4
# "Напишите функцию которая принимает в себя словарь где ключи это номера а значения страны. 
# Попросите пользователя ввести страну или ключ и выдайте ему результат."
# d = ({'1': 'kyrgyzstan'}, {'2': 'kazahstan'})
# a = input("ведите ключ или страну: ")
# def country(k):
#     for key, value in k.items():
#         if key in a:
#             print(value)
#         if value in a:
#             print(key)

# country({'1': 'kyrgyzstan', '2': 'kazahstan'})

#№5
# 'С помощью рекурсии выведите числа фибоначи'

# def memoize(func):
#     memo = dict()
#     def decorated(n):
#         if n not in memo:
#             memo[n] = func(n)
#         return memo[n]

#     return decorated

# @memoize
# def fib(n):
   
#     global call_count
#     call_count = call_count + 1
  

#     if n<=1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# call_count = 0 
# for i in range(100):
#     print(fib(i))
# print(call_count) 


#№6
# С помощью рекурсии выведите факториал'
# def fac(n):
#     if n == 0:
#         return 1
#         return fac(n-1) * n


# print(fac(10))
# def fac():
f = int(input("Enter a number whose factorial you want to calculate = "))
def fac(a):   
    # f = int(input("Enter a number whose factorial you want to calculate = "))
    while a < f:
        a = a*1
    print(a)
    fac(a + 1) 
fac(1)                                                                  
# for i in range(1,f): 
#     f=f*i 
          
# print(f) 



# 'С помощью рекурсии выполните перевод числа в двоичную систему счисления'
# "10 - 1010"
# "12 - 1100"
# "3 - 11"
# "15 - 1111""
# """
# l = []
# def cat(b):
#     if (b == 0):
#         return l
#     dick = b % 2
#     l.append(dick)
#     cat(b // 2)
# a = int(input("Введите число: "))
# cat(a)
# l.reverse()
# print("Двоичная форма числа:")
# for i in l:
#     print(i)

# """
# 'Найдите длину списка при помощи рекурсии'