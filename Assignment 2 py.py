# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:47:50 2019

@author: gilro
"""

#Week 2 assignment

import numpy as np
import pandas as pd
import time
import timeit

from random import seed
from random import random
import string

# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))

import random
import string

array_string5000 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(5000)]
array_string10000 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(10000)]
array_string15000 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(15000)]
array_string20000 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(20000)]
array_string25000 = [''.join(random.choices(string.ascii_letters, k = 5)) for _ in range(25000)]

print(selectionSort(array_string5000))

start_time = time.time()
selectionSort(array_string5000)
end_time = time.time()
selectionSort1 = (end_time - start_time)

start_time = time.time()
selectionSort(array_string10000)
end_time = time.time()
selectionSort2 = (end_time - start_time)

start_time = time.time()
selectionSort(array_string15000)
end_time = time.time()
selectionSort3 = (end_time - start_time)

start_time = time.time()
selectionSort(array_string20000)
end_time = time.time()
selectionSort4 = (end_time - start_time)

start_time = time.time()
selectionSort(array_string25000)
end_time = time.time()
selectionSort5 = (end_time - start_time)

selectionSort1 
selectionSort2
selectionSort3
selectionSort4
selectionSort5

selectionSort = np.array([selectionSort1, selectionSort2, selectionSort3, selectionSort4, selectionSort5])

k15array_string5000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(5000)]
k15array_string10000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(10000)]
k15array_string15000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(15000)]
k15array_string20000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(20000)]
k15array_string25000 = [''.join(random.choices(string.ascii_letters, k = 15)) for _ in range(25000)]


start_time = time.time()
selectionSort(k15array_string5000)
end_time = time.time()
k15selectionSort1 = (end_time - start_time)

start_time = time.time()
selectionSort(k15array_string10000)
end_time = time.time()
k15selectionSort2 = (end_time - start_time)

start_time = time.time()
selectionSort(k15array_string15000)
end_time = time.time()
k15selectionSort3 = (end_time - start_time)

start_time = time.time()
selectionSort(k15array_string20000)
end_time = time.time()
k15selectionSort4 = (end_time - start_time)

start_time = time.time()
selectionSort(k15array_string25000)
end_time = time.time()
k15selectionSort5 = (end_time - start_time)


k15selectionSort1
k15selectionSort2
k15selectionSort3
k15selectionSort4
k15selectionSort5

k15selectionSort = np.array([k15selectionSort1, k15selectionSort2, k15selectionSort3, k15selectionSort4, k15selectionSort5])

array_int5000 = list(np.random.randint(0,1000000, 5000))
array_int10000 = list(np.random.randint(0,1000000, 10000))
array_int15000 = list(np.random.randint(0,1000000, 15000))
array_int20000 = list(np.random.randint(0,1000000, 20000))
array_int25000 = list(np.random.randint(0,1000000, 25000))

start_time = time.time()
selectionSort(array_int5000)
end_time = time.time()
IntselectionSort1 = (end_time - start_time)

start_time = time.time()
selectionSort(array_int10000)
end_time = time.time()
IntselectionSort2 = (end_time - start_time)

start_time = time.time()
selectionSort(array_int15000)
end_time = time.time()
IntselectionSort3 = (end_time - start_time)

start_time = time.time()
selectionSort(array_int20000)
end_time = time.time()
IntselectionSort4 = (end_time - start_time)

start_time = time.time()
selectionSort(array_int25000)
end_time = time.time()
IntselectionSort5 = (end_time - start_time)

IntselectionSort1
IntselectionSort2
IntselectionSort3
IntselectionSort4
IntselectionSort5

IntselectionSort = np.array([IntselectionSort1, IntselectionSort2, IntselectionSort3, IntselectionSort4, IntselectionSort5])

array_float5000 = list(np.random.random(5000))
array_float10000 = list(np.random.random(10000))
array_float15000 = list(np.random.random(15000))
array_float20000 = list(np.random.random(20000))
array_float25000 = list(np.random.random(25000))

start_time = time.time()
selectionSort(array_float5000)
end_time = time.time()
floatselectionSort1 = (end_time - start_time)

start_time = time.time()
selectionSort(array_float10000)
end_time = time.time()
floatselectionSort2 = (end_time - start_time)

start_time = time.time()
selectionSort(array_float15000)
end_time = time.time()
floatselectionSort3 = (end_time - start_time)

start_time = time.time()
selectionSort(array_float20000)
end_time = time.time()
floatselectionSort4 = (end_time - start_time)

start_time = time.time()
selectionSort(array_float25000)
end_time = time.time()
floatselectionSort5 = (end_time - start_time)

floatselectionSort1
floatselectionSort2
floatselectionSort3
floatselectionSort4
floatselectionSort5

floatselectionSort = np.array([floatselectionSort1, floatselectionSort2, floatselectionSort3, floatselectionSort4, floatselectionSort5])

import prettytable
from prettytable import PrettyTable
t = PrettyTable(['array string 5', 'array string 15', 'array int', 'array float'])
t.add_row([selectionSort1, k15selectionSort1, IntselectionSort1, floatselectionSort1])
t.add_row([selectionSort2, k15selectionSort2, IntselectionSort2, floatselectionSort2])
t.add_row([selectionSort3, k15selectionSort3, IntselectionSort3, floatselectionSort3])
t.add_row([selectionSort4, k15selectionSort4, IntselectionSort4, floatselectionSort4])
print(t)


import seaborn as sns
import matplotlib.pyplot as plt

array5lenght1 = len(array_string5000)
array5lenght2 = len(array_string10000)
array5lenght3 = len(array_string15000)
array5lenght4 = len(array_string20000)
array5lenght5 = len(array_string25000)

array5length = np.array([array5lenght1, array5lenght2, array5lenght3, array5lenght4, array5lenght5])

array15lenght1 = len(k15array_string5000)
array15lenght2 = len(k15array_string10000)
array15lenght3 = len(k15array_string15000)
array15lenght4 = len(k15array_string20000)
array15lenght5 = len(k15array_string25000)

array15length = np.array([array15lenght1, array15lenght2, array15lenght3, array15lenght4, array15lenght5])

int_lenght1 = len(array_int5000)
int_lenght2 = len(array_int10000)
int_lenght3 = len(array_int15000)
int_lenght4 = len(array_int20000)
int_lenght5 = len(array_int25000)

int_length = np.array([int_lenght1, int_lenght2, int_lenght3, int_lenght4m, int_lenght5])

float_lenght1 = len(array_float5000)
float_lenght2 = len(array_float10000)
float_lenght3 = len(array_float15000)
float_lenght4 = len(array_float20000)
float_lenght5 = len(array_float25000)

float_lenght = np.array([float_lenght1, float_lenght2, float_lenght3, float_lenght4, float_lenght5])

plt.plot(array5length, selectionSort)
plt.plot(array15length, k15selectionSort)
plt.plot(int_length, IntselectionSort)
plt.plot(float_lenght, floatselectionSort)
