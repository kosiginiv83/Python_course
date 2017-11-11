"""
Домашнее задание для лекции "Задачки на собеседованиях для продвинутых,
с тонкостями языка"

Описание
    1. Перестроить заданный связанный список (LinkedList) в обратном порядке.
    Для этого использовать метод `LinkedList.reverse()`, представленный
    в данном файле.
    2. Определить сложность алгоритма.
    3. Определить потребление памяти в big-O notation.

"""


from typing import Iterable


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None  # type: LinkedListNode


class LinkedList:

    def __init__(self, values: Iterable):
        previous = None
        self.head = None
        for value in values:
            current = LinkedListNode(value)
            if previous:
                previous.next = current
            self.head = self.head or current
            previous = current

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def reverse(self):
        temp_list = []
        for unit in self:
            temp_list.append(unit)
        rev_temp_list = reversed(temp_list)
        return LinkedList(rev_temp_list)
    
    @property
    def print(self):
        for unit in self:
            print(unit)


linked_list = LinkedList([1, 2, 3, 4])
linked_list.print
print('linked_list.head.data:', linked_list.head.data)
print('=========================')

reversed_list = linked_list.reverse()
reversed_list.print
print('reversed_list.head.data:', reversed_list.head.data)