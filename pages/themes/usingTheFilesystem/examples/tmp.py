import sys
from functools import reduce

x = 1000
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

int_object_memory = sys.getsizeof(x)
list_object_memory = sys.getsizeof(l)
list_elements_memory = sum(sys.getsizeof(el) for el in l)

print(int_object_memory)  # 28
print(list_object_memory)  # 136
print(list_elements_memory)  # 280
