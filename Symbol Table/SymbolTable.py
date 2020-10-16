from HashTable import HashTable

SIZE = 10;

class SymbolTable:
    def __init__(self):
        self.__hash_table = HashTable(SIZE)

    def insert(self, elem):
        return self.__hash_table.add(elem)

    def search(self, elem):
        return self.__hash_table.index(elem)