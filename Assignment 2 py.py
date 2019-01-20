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

selectionSort = np.array([selectionSort1, selectionSort2, selectionSort3, selectionSort4])

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

k15selectionSort = np.array([k15selectionSort1, k15selectionSort2, k15selectionSort3, k15selectionSort4])