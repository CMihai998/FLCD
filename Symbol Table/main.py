from SymbolTable import SymbolTable

if __name__ == '__main__':
    symbol_table = SymbolTable()

    print("Running tests")
    positions = [symbol_table.insert("ana"),
                 symbol_table.insert("are"),
                 symbol_table.insert("are"),
                 symbol_table.insert("naa")]

    assert symbol_table.search("ana") == positions[0]
    assert symbol_table.search("are") == positions[1]
    assert symbol_table.search("naa") == positions[3]
    assert symbol_table.search("pere") == -1
    print("Tests done")
    print(symbol_table)
