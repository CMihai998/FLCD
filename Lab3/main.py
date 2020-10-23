from dataStructures.SymbolTable import SymbolTable
from scanner.ProgramInternalForm import ProgramInternalForm
from scanner.Scanner import Scanner

if __name__ == '__main__':
    st = SymbolTable()
    pif = ProgramInternalForm()
    scn = Scanner()
    error_msg = ''

    file_name = "programs/p2gresit.txt"

    with open(file_name) as file:
        for index, line in enumerate(file):
            tokens = scn.tokenize(line)

            for token in tokens:
                if scn.is_operator(token) or len(token) == 1 and scn.is_separator(token) or scn.is_reserved_word(token):
                    if token != ' ':
                        pif.add(token, 0)
                elif scn.is_constant(token) or scn.is_identifier(token):
                    pif.add(token, st.search(token) if st.search(token) != -1 else st.insert(token))
                else:
                    error_msg += "\nError at line " + str(index) + " caused by token " + token

    print(st)
    print(pif)
    print(error_msg)
