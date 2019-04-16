
# coding: utf-8

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# In[ ]:


import random

bubbles = [random.randint(-100,100) for x in range(5)] 
print('initial: ', bubbles)
n = 1 

while n < len(bubbles): 
    for i in range(len(bubbles)-n):
        if bubbles[i] > bubbles[i+1]:
            bubbles[i], bubbles[i+1] = bubbles[i+1], bubbles[i]
    n += 1

print('sorted: ', bubbles)


# # po polochkam
# import random
# 
# bubbles = [random.randint(-100,100) for x in range(5)]
# print('initial: ', bubbles)
# n = 1
# print('len(bubbles) = ',len(bubbles))
# print('while n < len(bubbles): ', n)
# 
# while n < len(bubbles):
#     print('len(bubbles)-n ', len(bubbles)-n)
#     
#     for i in range(len(bubbles)-n):
#         print('for i in range(len(bubbles)-n)', i)
#         if bubbles[i] > bubbles[i+1]:
#             print('bubbles[i] > bubbles[i+1] ')
#             print('i = ',i)
#             print( f'bubbles[{i}], bubbles[{i+1}] = bubbles[{i+1}], bubbles[{i}]')
#             bubbles[i], bubbles[i+1] = bubbles[i+1], bubbles[i]
#         n += 1
#         print('n= ', n)
# print('sorted: ', bubbles)

# In[ ]:


#1 метод сортировки выборкой

import random

massiv = [random.randint(-100,100) for x in range(5)]


print('initial ', massiv)


sorted_massiv = massiv[:]

for i in range(len(sorted_massiv)):
    ind_min = i
    for j in range(i+1, len(sorted_massiv)):
        if sorted_massiv[j] < sorted_massiv[ind_min]:
            ind_min = j
    sorted_massiv[ind_min],sorted_massiv[i] = sorted_massiv[i], sorted_massiv[ind_min]

print('sorted ', sorted_massiv)


# In[ ]:


# po polochkam
##sorted_massiv = massiv[:]#####

#for i in range(len(sorted_mass#iv)):
#    ind_min = i
#    print('next ind_min = i ', ind_min )
#    print('sorted_massiv[ind_min] = ', sorted_massiv[ind_min])
#    for j in range(i+1, len(sorted_massiv)):
#        print('next j = ', j)
#        print('sorted_massiv[j] ',sorted_massiv[j])
#        if sorted_massiv[j] < sorted_massiv[ind_min]:
#            ind_min = j
#            print('ind_min = j ', j)
#        print(sorted_massiv)
#    sorted_massiv[ind_min],sorted_massiv[i] = sorted_massiv[i], sorted_massiv[ind_min]
#    print(sorted_massiv)

#print('sorted ', sorted_massiv)
#[35, -72, -59, -58, 91]


# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# In[13]:


import random

m = 6

mas = [random.randint(0,50) for x in range(2*m+1)] 

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)
sorted_mas = quicksort(mas)

print('initial:', mas)
print('sorted: ', sorted_mas)
print('median = ', sorted_mas[m])

