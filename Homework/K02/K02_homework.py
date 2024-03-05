from timeit import Timer
from big_o import big_o, datagen
import random
# 估算 append 函数和 insert 的大 O 表示
def list_insert(lst):
    return lst.insert(0, random.random())
def list_append(lst):
    return lst.append(random.random())

best, others = big_o(
    list_insert,
    lambda n: datagen.integers(n, 1, 5),
    min_n = 10000,
    max_n = 100000,
    n_measures = 10,
    n_repeats = 100,
)
print(best)

best, others = big_o(
    list_append,
    lambda n: datagen.integers(n, 1, 5),
    min_n = 10000,
    max_n = 100000,
    n_measures = 10,
    n_repeats = 100,
)
print(best)

