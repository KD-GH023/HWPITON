'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
Последняя строка содержит число X.
*Пример:*
5
 7 -2 3 5 1
3
-> 1'''
N=int(input("Введите количество элементов в массиве:" ))
import random
lst = [random.randint(1, 50) for _ in range(N)]
print(lst)
X=int(input("Введите искомое число:" ))
count=0
for i in range(len(lst)-1):
    if lst[i] == X:
        count += 1
print(count)




