from dataStructures.HashTable import HashTable

SIZE = 13

class SymbolTable:
    def __init__(self):
        self.__hash_table = HashTable(SIZE)

    def insert(self, elem):
        return self.__hash_table.add(elem)

    def search(self, elem):
        return self.__hash_table.index(elem)

    def __str__(self):
        return self.__hash_table.__str__()