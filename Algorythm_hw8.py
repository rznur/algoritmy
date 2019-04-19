
# coding: utf-8

#  Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

# In[51]:


string = 'matchhashhashhashmatchstring'

combs = [hashlib.sha1(k.encode('utf-8')).hexdigest() for k in string]

for  i in range(1,len(string)-1):
    combs.append(hashlib.sha1(string[:-i].encode('utf-8')).hexdigest())
    combs.append(hashlib.sha1(string[i:].encode('utf-8')).hexdigest())
len(set(combs))


# In[50]:


string = 'matchhashhashhashmatchstring'

combs = [k for k in string]

for  i in range(1,len(string)-1):
    combs.append(string[:-i])
    combs.append(string[i:])
len(set(combs))


# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

# In[ ]:


# не успеваю разобрать материал

