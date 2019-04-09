
# coding: utf-8

# In[ ]:


###### 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала 
#(т.е. 4 отдельных числа) для каждого предприятия.. 
#Программа должна определить среднюю прибыль (за год для всех предприятий) и 
#вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, 
#чья прибыль ниже среднего.

from collections import namedtuple
from numpy import mean

company_num = int(input('number of companies: '))

BusinessRecord = namedtuple('BusinessRecord', 'name,Q1profit, Q2profit, Q3profit, Q4profit')
BusinessRecordAnalysis = namedtuple('BusinessRecordAnalysis', BusinessRecord._fields + ('avg_profit',))

n = 0
d = []
avg_prof_lst = []

while n < company_num:
    company = BusinessRecord(name = input('\nname: '), Q1profit = input('Q1profit: '), Q2profit = input('Q2profit: '), Q3profit = input('Q1profit: '), Q4profit = input('Q4profit: '))
    
    avg_profit = (int(company.Q1profit) + int(company.Q2profit) + int(company.Q3profit) + int(company.Q4profit))/4
    company_analysis = BusinessRecordAnalysis(company.name, company.Q1profit, company.Q2profit, company.Q3profit, company.Q4profit, avg_profit = avg_profit)
    print(f'\t\t\t\t\t\taverage yearly profit for {company.name} is {avg_profit}')
    d.append(company_analysis)
    avg_prof_lst.append(avg_profit) 
        
    n += 1

mean_of_companies_profits = mean(avg_prof_lst)

#print('\n', d)
print(f'\naverage profit among companies is {mean_of_companies_profits}')

above_avg = []
below_avg = []
for bus_rec in d:
    #print('\n', bus_rec.avg_profit)
    if bus_rec.avg_profit >= mean_of_companies_profits:
        above_avg.append(bus_rec.name)
    else:
        below_avg.append(bus_rec.name)
#for the sake of simplicity I don't bother  with mean vs average differences

print(f'\nCompanies with profits above mean: {above_avg}')
print(f'\nCompanies with profits below mean: {below_avg}')
        





# In[ ]:


#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
#При этом каждое число представляется как массив, элементы которого это цифры числа. 
#Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
#Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


#Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections


# In[2]:


first = input()
second = input()

list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
                                              # A=10; B=11; C=12; D=13; E=14; F=15
if len(first) > len(second):
    first, second = second, first
    
second = second[::-1]
third = []
print(first, second) 
#4AD 6C



j = -1
k = 0
for i in second:
    one = list_of_numbers.index(i)
    #print('(i) ', i)
    #print('one= ', one)
    two = list_of_numbers.index(first[j])
    #print('(first[j]) ', first[j])
   # print ('two= ',two)
   # print('(one + two + k) % 16 = ', (one + two + k) % 16)
    third.append(list_of_numbers[(one + two + k) % 16])
   # print('third= ', third)
    if (one + two) >= 15:
        k = 1
      #  print('k= ',k)
    else:
        k = 0
      #  print('k= ',k)
    j -= 1
    #print('j= ', j)
    if j == -len(first)-1:
       # print('j == -len(first)-1 ', j)
        break
diff = len(second) - len(first)
 #False == 0
    # True == 1 or non-empty - in Python, every non-empty value is treated as true
    
if diff:
    for i in second[-diff:]:
        third.append(list_of_numbers[(list_of_numbers.index(second[-diff])+k)%16])
    if list_of_numbers.index(second[-diff])+1 >=15:
        k = 1
    else:
        k = 0
if k == 1:
    third.append('1')

print(third[::-1])


# 16-ричные не понимаю, поэтому использовала гугл. но все разобрала. осталось придумать как это заменить на collections
# 
# source: http://www.cyberforum.ru/blogs/1407093/blog5748.html
# 
# Возьмём пример поинтереснее, чем в условии. Предположим, нам на вход подаются значения в таком виде 2A2, FFD5F. Кстати, переводить их не за чем в списки. Ну если надо, то list(string) Вам в этом поможет.
# 
# PythonВыделить код
# 1
# 2
# first = input()
# second = input()
# Если даже и приходят в другом виде, то преобразовать к такому, думаю, особого труда не составит.
# Итак, создаём список из элементов 16-ричной системы
# 
# PythonВыделить код
# 1
# list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
# Сравниваем 2 входных строки и выбираем большую для итераций по её символам.
# 
# PythonВыделить код
# 1
# 2
# if len(first) > len(second):
#   first, second = second, first
# Переворачиваем выбранную строку. Мне так удобней просто работать с ней.
# и создаём третий список куда будем добавлять новые, найденные элементы.
# 
# PythonВыделить код
# 1
# 2
# second = second[::-1]
# third = []
# Создаём вспомагательные переменные и запускаем цикл по большей строке. В нём находим индексы соответствующих элементов первой и второй строк в созданном ранее списке символов 16-ричной системы. Если у нас есть переход в другой разряд, то прибавляем k = 1, если нет, то k = 0. Чтоб не вывалится за границы, берём остаток от деления. C той же целью введён break.
# PythonВыделить код
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# j = -1
# k = 0
# for i in second:
#   one = list_of_numbers.index(i)
#   two = list_of_numbers.index(first[j])
#   third.append(list_of_numbers[(one + two + k) % 16])
#   if (one + two) >= 15:
#     k = 1
#   else:
#     k = 0
#   j -= 1
#   if j == -len(first)-1:
#     break
# Как только цикл закончен, проверям, отличались ли у нас вообще числа. Если да, то проходим по оставшимся символам большей строки и прибавляем их. Внимание! Тут нам приходится та же переменная k. Ведь могло быть такое, что последний элемент последней итерации предыдущего цикла перешёл в другой разряд. Мы это и учитываем благодаря переменной k.
# PythonВыделить код
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# diff = len(second) - len(first)
#  
# if diff:
#   for i in second[-diff:]:
#     third.append(list_of_numbers[(list_of_numbers.index(second[-diff])+k)%16])
#     if list_of_numbers.index(second[-diff])+1 >=15:
#       k = 1
#     else:
#       k = 0
# Ну и если после последний итерации этого цикла у нас число перешло в другой разряд, то просто добавляем ещё одну еденицу.
# PythonВыделить код
# 1
# 2
# if k == 1:
#   third.append('1')
# Ну и переворачиваем список в нужный нам вид
# PythonВыделить код
# 1
# print(third[::-1])
# 
