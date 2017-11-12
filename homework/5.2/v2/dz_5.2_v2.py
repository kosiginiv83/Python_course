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
        #self.length = len(values)
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
        reversed_list = LinkedList([])
        current = self.head
        previous = None
        while current.next:
            current_2 = self.head
            while current_2.next:
                print('++++++++++++++++++++')
                if previous:
                    previous.next = current_2
                if not(reversed_list.head):
                    reversed_list.head = current_2
                previous = current_2
                current_2 = current_2.next
            print('======================')
            node = LinkedListNode(current_2.data)
            current_2 = None
            current = current.next
        return reversed_list
            
    
    @property
    def print(self):
        for unit in self:
            print(unit)


linked_list = LinkedList([1, 2, 3, 4])
linked_list.print
#print('linked_list.head.data:', linked_list.head.data)
print('=========================')

#reversed_list = LinkedList([])
reversed_list = linked_list.reverse()
reversed_list.print

#print('reversed_list.head.data:', reversed_list.head.data)
