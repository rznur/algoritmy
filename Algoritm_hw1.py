
# coding: utf-8

# In[5]:


#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


while True:
    exit = 'exit', 'Exit', 'EXIT', 'EXit', 'EXIt', 'exiT', 'eXIT'
    # 1 step - input
    number = input('Please input 3 digits number. Or type in "exit" to exit. ' )
    if number in exit:
        print('Program is finished. Thank you')
        break
        
    while len(number) == 3:
        
        try:
            fig1 = int(number[0])
            fig2 = int(number[1])
            fig3 = int(number[2])
            print('sum of digits = ', fig1 + fig2 + fig3)
            print('multiplication of digits = ', fig1 * fig2 * fig3)
            break
        except ValueError:
            print('Input is not a number. Please re-input the number that consists of 3 digits')
            break
        
    if len(number) !=3:
        print('Input value is wrong. 3 digits integer is required. Please re-input')
        continue
    

    


# In[4]:


#2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
# SKAJU SRAZU pobitovye operacii ne ponimau, skolko ne pytalas (nadeus oni mne ne prigodyatsa, po krainei mere na rannih porah data science i AI), reshenie iz interneta.Ostalnye zadachi - sama.
a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))
 
print("%d & %d = %d (%s)" % (a,b,a&b,bin(a&b)))
print("%d | %d = %d (%s)" % (a,b,a|b,bin(a|b)))
print("%d ^ %d = %d (%s)" % (a,b,a^b,bin(a^b)))
print("%d << 2 = %d (%s)" % (b,b<<2,bin(b<<2)))
print("%d >> 2 = %d (%s)" % (b,b>>2,bin(b>>2)))


# In[6]:


#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
# решение без цикла (для разнообразия :) ,т.к. 1-е задание в цикле)
# input
try:
    x1 = int(input('Введите координату Х для точки А: '))
    y1 = int(input('Введите координату Y для точки А: '))
    x2 = int(input('Введите координату Х для точки B: '))
    y2 = int(input('Введите координату Y для точки B: '))

    # getting k
    k = (y1 - y2) / (x1 - x2)
    #getting b
    b = y2 - k * x2

    print('Уравнение прямой с заданными координатами двух точек: y = {}x + {}'.format(k,b))
except ValueError:
    print('Координаты точек должны быть числами')
    


# In[ ]:


# 4. Написать программу, которая генерирует в указанных пользователем границах:
#случайное целое число;
#случайное вещественное число;
#случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от #'a' до 'f', то вводятся эти символы. 
#Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

while True:
    try:
        print("\n\n\t\t 1 = cлучайное целое число \n\t\t 2 = случайное вещественное число \n\t\t 3 = случайный символ\n\t\t 4 = EXIT\n") 
        task=int(input('Пожалуйста, введите номер  :\n')) 

    #cлучайное целое число;
        if task == 1:
            try:
                #random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
                print('\nВыполняется генерация случайного целого числа N, где A ≤ N ≤ B.')


                A = int(input('\nВведите число А (нижнюю границу диапазона): '))
                B = int(input('Введите число B (верхнюю границу диапазона): '))

              #  if isinstance(int(A), int) and isinstance(int(B), int):
               #     A = int(A)
                #    B = int(B)
                print(f'Сгенерированное случайное число в диапазоне от {A} до {B} равно {random.randint(A, B)}. ')
                                            
            except ValueError or TypeError:
                print('\nГраницы диапазона должны быть целыми числами и удовлетворять условию A ≤ N ≤ B. Повторите ввод')
                
    #случайное вещественное число;
        if task ==2:
            #random.uniform(start, stop)
            try:
                print('\nВыполняется генерация случайного вещественного числа N в диапазоне от А до В.')
                A = float(input('\nВведите число А (начало диапазона): '))
                B = float(input('Введите число B (конец диапазона): '))
                print(random.uniform(A,B))
                
            except ValueError:
                print('\n Необходимо ввести вещественное число, а не символ или букву. Пожалуйста, повторите ввод. ')
        
    #случайный символ.
        if task == 3:
            
            try:
            
                import string
                print("Для Вашего удобства последовательность символов и знаков приведена ниже (English portion only)\n")
                print(string.printable)

                print('Границы диапазона необходимо задавать последовательно (слева направо, а не наоборот)')

                #try:
                symb_1 = ord(input('Введите первый символ: '))
                symb_2 = ord(input('Введите второй символ: '))
                print(chr(random.randint(symb_1, symb_2)))

            except ValueError or TypeError:
                print("Границы диапазона необходимо задавать последовательно (слева направо, а не наоборот).\nПожалуйста повторите ввод. ")
    #exit
        if task == 4:
            print('Программа завершила работу')
            break
        
    except ValueError:
        print('\n\n\n\t\t\t\t\t\t Неправильно выбранный номер действия. Введите номер согласно меню: 1, 2, 3 или 4')
        


# In[7]:


#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
letter1 = input('please type in first letter: ')
letter2 = input('please type in second letter: ')

print('First letter place order is: ', ord(letter1))
print('Second letter place order is: ', ord(letter2))
print('There are {} characters between these two letters in UTF-8 map'. format(abs(ord(letter1)-ord(letter2))))


# In[8]:


#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#assuming upper and lowercase english letters only

let_num = int(input('please type in letter number from 65 to 90 or 97 to 122: '))

if 65<let_num<90 or 97<let_num<122:
    print('This number is for letter: ', chr(let_num))
else:
    print('No letter (Eng) assigned to this number')


# In[3]:


#7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, 
#составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, 
#равнобедренным или равносторонним.

print('Введите значение отрезков a,b,c')
a = int(input("Сторона a = "))
b = int(input("Сторона b = "))
c = int(input("Сторона c = "))


# Сумма длин двух сторон треугольника должна быть больше третьей стороны. 
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник с заданными длинами отрезков не существует")
    
elif a != b and a != c and b != c:
    print("Треугольник с заданными отрезками существует! Тип: разносторонний")
elif a == b == c:
    print("Треугольник с заданными отрезками существует! Тип: равносторонний")
else:
    print("Треугольник с заданными отрезками существует! Тип: равнобедренный")


# In[9]:


#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Input year that you want to check:'))

#обычный год
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):  
    print(f'{year} is regular year')

else:  # високосный год

    print (f'{year} is leap year')


# In[10]:


#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input('Первое число: '))
b = float(input('Второе число: '))
c = float(input('Третье число: '))

if a > b:
    if c<b:
        print(b)
    elif a>c:
        print(c)
    else:
        print(a)
elif a<b:
    if c>b:
        print(b)
    elif a<c:
        print(c)
    else:
        print(a)
else:
    print('Числа равны')
#   
#a>b i c<b - c<b<a - b
# a>b i c>b - b<c  b<a  - elif a>c - c, else a

# a<b i c>b - a<b<c  - b
# a<b i c<b - a<b c<b  , than if a<c, print c, else a

