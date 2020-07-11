#cache zapamietuja wyniki dla poszczegolnych wynikow funckji.
#w naszym przykladzie jak liczy 3! do czego musial policzyc 2! a zrobil to w poprzednim
#kroku, to teraz nie mus

import functools

@functools.lru_cache()
def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

for i in range(1,11):
    print('{}! = {}'.format(i,Factorial(i)))

print(Factorial.cache_info())

