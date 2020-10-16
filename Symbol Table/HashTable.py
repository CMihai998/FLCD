from pprint import pprint

class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__items = [[] for _ in range(size)]

    def index(self, elem):
        position = self.hash(elem)
        if elem in self.__items[position]:
            return position

        return -1

    def hash(self, elem):
        return sum(ord(letter) for letter in list(elem)) % self.__size

    def add(self, elem):
        position = self.index(elem)
        if position != -1:
            return position;

        position = self.hash(elem)
        self.__items[position].append(elem)

        return position

    def __str__(self):
        return self.__items.__str__()