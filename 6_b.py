"""
6. Реализовать два небольших скрипта:
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.

Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""
from itertools import cycle
import sys

MAX_CYCLE = 3

def generator(iterable):
    S = 0
    for i in cycle(iterable):
        if S > MAX_CYCLE * len(iterable):
            return
        yield i
        S += 1

if __name__ == "__main__":
    [print(i) for i in generator(sys.argv[1:])]