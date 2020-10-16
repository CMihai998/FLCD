class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__items = [[] for _ in range(size)]

    def index(self, elem):
        for index, lst in enumerate(self.__items):
            if elem in lst:
                return index

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