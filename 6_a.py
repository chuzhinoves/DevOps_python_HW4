"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3,
а при достижении числа 10 завершаем цикл.
"""

from itertools import count
import sys

MAX_NUMB = 10

def generator(start):
    for i in count(start):
        if i > MAX_NUMB:
            return
        yield i

     
if __name__ == "__main__":
    [print(i) for i in generator(int(sys.argv[1]))]