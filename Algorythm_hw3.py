
# coding: utf-8

# In[ ]:


#1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

total_count = 0
count_per_num = [0]*8
#print(count_per_num)

for i in range (2, 100):
   for m in range(2,10):
       if i % m == 0:
           total_count += 1
           count_per_num[m-2] += 1 # [m-2] - chtoby v massive                      [0, 0, 0, 0, 0, 0, 0, 0] 
                                   # u 2-ki bylo mesto pod nomer 0                 [2, 3, 4, 5, 6, 7, 8, 9]

           
print('Total:', total_count)   
#print(count_per_num)

n = 0

while n < len(count_per_num):
   print(f'\n{n+2} - {count_per_num[n]}')
   n += 1


# In[ ]:


# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
#то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
#т.к. именно в этих позициях первого массива стоят четные числа.


m = [8, 3, 15, 6, 4, 2]
m2 = []
for i, val in enumerate(m):
    if val % 2 == 0:
        m2.append(i)
    #print(f'{i} - {val}')
print(m2)


# In[ ]:


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
r = []
for i in range(0,10):
    r.append(random.randint(1,100))
print(r)

minimum = min(r)
maximum = max(r)

ind_min = r.index(minimum)
ind_max = r.index(maximum)
print(f'for minimumm {minimum} index =  {ind_min},\nfor maximum {maximum} index = {ind_max}')
print('\nafter switching, it looks like this: ')
r[ind_min], r[ind_max] = r[ind_max], r[ind_min]
print(r)


# In[ ]:


# 4. Определить, какое число в массиве встречается чаще всего.
from random import random

n = 100

mas = [0] * n

for i in range(n):
    mas[i] = int(random() * 5)
    
print(mas)

val = mas[0]
most_freq = 1

for i in range(n-1):
    freq = 1
    for m in range(i+1,n):
        if mas[i] == mas[m]:
            freq += 1
    if freq > most_freq:
        most_freq = freq
        val = mas[i]

if most_freq > 1:
    print(f'\n{val} is the most frequent number, it repeats {most_freq} times')
else:
    print('no repeats')


# In[ ]:


#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

n = 10
mas = [0] * n
start = -100
end = 100

for i in range(n):
    mas[i] = int(random.uniform(start, end))
print(mas)

mas_neg = []

j = 0
ind = -1

while j < n:
    if mas[j] < 0 and ind == -1:
        ind = j
    elif mas[j] < 0 and mas[j] > mas[ind]:
        ind = j
    j += 1
        
print(f'\nlocation index (counting starts from 1) = {ind+1}: value at this location is {mas[ind]}' )


# In[ ]:


#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.

import random

n = 10
mas = [0] * n
start = -100
end = 100

for i in range(n):
    mas[i] = int(random.uniform(start, end))
print(mas)

minimum = min(mas)
maximum = max(mas)
to_sum = 0

ind_min = mas.index(minimum)
ind_max = mas.index(maximum)

start = ind_min
end = ind_max

if ind_min > ind_max:
    start = ind_max
    end = ind_min


print(f'for minimumm {minimum} index =  {ind_min},\nfor maximum {maximum} index = {ind_max}')


for n in range(start+1, end):
    to_sum += mas[n]
    
print(f'sum of elements between indexes {start} and {end} equals : {to_sum}')


# In[ ]:


#7. В одномерном массиве целых чисел определить два наименьших элемента. 
#Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

n = 10
mas = [0] * n
start = -100
end = 100

for i in range(n):
    mas[i] = int(random.uniform(start, end))
print(mas)

min1 = min(mas)
mas.pop(mas.index(min1))
#new mas without min1 poped out
min2 = min(mas)

print(f'\ntwo minimum values from this list are {min1} and {min2}')


# In[ ]:


#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
#Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
#В конце следует вывести полученную матрицу.
M = 5
N = 4

mtrx = []

for i in range(N):
    line = []
    el_sum = 0
    print(f'line {i}')
    for j in range(M-1):
        n = int(input())
        el_sum += n
        line.append(n)
    line.append(el_sum)
    mtrx.append(line)

for i in mtrx:
    print(i)


# In[ ]:


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


# In[6]:


# решение без NumPy

import random

a = []
#k = 10 # просто начальное значение, может быть любым
ot = -198
do = 899
N= 4
M = 5

for r in range(N): # 4 строк
    a.append([]) # создаем пустую строку
    for c in range(M): # в каждой строке - 5 элементов
        k = int(random.randrange(ot, do))
        a[r].append(k) # добавляем очередной элемент в строку
        k += 1 # увеличиваем значение счетчика

for r in a:
    print(r)

max_el = max(max(x) for x in a)  
min_el = min(min(x) for x in a) 

mx = min_el - 1
 
for j in range(M): # stolbec
    mn = max_el + 1
    for i in range(N): # stroka
        #print(a[i][j])
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("Максимальный среди минимальных: ", mx)

