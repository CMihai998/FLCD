class HashTable:
    def __init__(self, size):
        self.__size = size
        self.__items = [set() for _ in range(size)]

    def index(self, elem):
        position = self.hash(elem)
        if elem in self.__items[position]:
            return position

        return -1

    def hash(self, elem):
        return sum(ord(letter) for letter in list(elem)) % self.__size

    def add(self, elem):
        position = self.hash(elem)
        self.__items[position].add(elem)

        return position

    def __str__(self):
        result = ''
        for index, elem in enumerate(self.__items):
            result += str(index) + ':' + elem.__str__() + '\n'
        return result
