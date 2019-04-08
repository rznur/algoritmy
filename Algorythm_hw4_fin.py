
# coding: utf-8

# In[ ]:


#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

#из урока 2 /задание #1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
#Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, 
#а должна запрашивать новые данные для вычислений. 
#Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
##Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
#Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

                ############ Решение в лоб  #################

#set cycle 
#input
#perform task
#print res
#end cycle
import random

def reshenie_v_lob():

    print("\t\t\t\t\t Базовые математические операции с двумя числами") 

    while True:

        try:
            print('для завершения программы введите 0 в качестве знака')

            #val1 = int(input('Пожалуйста, введите первое число  :\n'))
            #val2 = int(input('Пожалуйста, введите второе число :\n'))
            #sign = input('Пожалуйста, введите знак :\n')
            val1 = random.randint(-10000,10000)
            val2 = random.randint(-10000,10000)
            signs = '+', '-', '*', '/', '+', '-', '*', '/', '0'  # repeated signs several times to increase in order to increase the frequence of choice of signs, not 0
            sign = random.choice(signs)

            if sign not in signs:
                print('Неверный знак. Повторите ввод одного из знаков: 0, +, -, *, / ' )

            if sign == '+':
                print("Результат сложения равен ", val1+val2)

            if sign == '-':
                print("Результат вычитания равен ", val1-val2)

            if sign == '*':
                print("Результат умножения равен ", val1*val2)

            if sign == '/':
                if val2 != 0:
                    print("Результат деления равен ", val1/val2)
                else:
                    print('невозможно произвести деление на 0')

            if sign == '0':
                print('завершение программы')
                break

        except ValueError:
            print('Неправильно введенные данные. Повторите ввод чисел и знаков')

reshenie_v_lob()


# In[ ]:


print('Анализ скорости "решение в лоб"')

import timeit

statement = 'reshenie_v_lob()'
setup = setup = "from __main__ import reshenie_v_lob"

prog_time = timeit.timeit(statement, setup, number = 5)
print(f' Программа выполняется за {prog_time} секунд')


# In[ ]:


############ красивое решение ###################
#
import operator #библиотека в которой описаны функции для сложения, умножения и тд для двух чисел
import random

operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
}

def krasivoe_reshenie():
  
    #
    while True:
        first_num =  random.randint(-10000,10000)
        second_num =  random.randint(-10000,10000)
        signs = '+', '-', '*', '/', '+', '-', '*', '/', '0' 
        operator = random.choice(signs)
    #
        if operator == '0':
            print("Goodbye")
            break
    #
        if operator not in operations:
            print("Not valid operator. Expected -+*/ or 0 for exit")
        else:
            if operator == '/':
                if second_num == 0:
                    print("Zero division error")
                    continue
    #
            print(operations[operator](first_num, second_num))
krasivoe_reshenie()


# In[ ]:


print('Анализ скорости "красивое решение"')

import timeit

statement = 'krasivoe_reshenie()'
setup = setup = "from __main__ import krasivoe_reshenie"

prog_time = timeit.timeit(statement, setup, number = 5)
print(f' Программа выполняется за {prog_time} секунд')


# In[ ]:


# raznica ne ochen bolshaya - 0.004 i 0.002 sekund.


# In[ ]:


### Prime numbers
# 2.Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


# In[2]:


def derevyannoe_reshenie():
    n = 1000
    # создаем пустой список для хранения простых чисел
    lst = []
    # в k будем хранить количество делителей
    k = 0
    # пробегаем все числа от 2 до N
    for i in range(2, n+1):
        #print("***i=",i)
        # пробегаем все числа от 2 до текущего
        for j in range(2, i):
           # print('j=',j)
            # ищем количество делителей
            if i % j == 0:
                k = k + 1
                #print('for k=',k)
        # если делителей нет, добавляем число в список
        if k == 0:
          #  print('if k=',k)
            lst.append(i)
        else:
            k = 0
            #print('else k=',k)
    # выводим на экран список
    print(lst)

#derevyannoe_reshenie()


# In[4]:


print('Анализ скорости derevyannoe_reshenie')

import timeit

statement = 'derevyannoe_reshenie()'
setup = setup = "from __main__ import derevyannoe_reshenie"

prog_time_derev = timeit.timeit(statement, setup, number = 5)
print(f' Программа выполняется за {prog_time_derev} секунд')


# In[5]:


def bystroe_reshenie():
    from math import sqrt
    n = 1000
    lst=[2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    print(lst)
bystroe_reshenie()


# In[6]:


print('Анализ скорости bystroe_reshenie')

import timeit

statement = 'bystroe_reshenie()'
setup = setup = "from __main__ import bystroe_reshenie"

prog_time_bystr = timeit.timeit(statement, setup, number = 5)
print(f' Программа выполняется за {prog_time_bystr} секунд')


# In[7]:


times = prog_time_derev/prog_time_bystr
print(f'optimized algorythm is {times} faster')

