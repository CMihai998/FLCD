import re

from finite_automation import FiniteAutomaton
from scanner.Tokens import Tokens


class Scanner:

    def __init__(self):
        self._tokens = Tokens()
        self.fa_identifier = FiniteAutomaton("input.json", deterministic=True)
        self.fa_constant = FiniteAutomaton("input2.json", deterministic=False)

    def tokenize(self, line):
        token_list = []
        index = 0
        token = ''

        while index < len(line):

            if self.is_part_of_operator(line[index]):
                possible_operator = self.get_operator_token(line, index)

                if possible_operator[0] is not None:
                    index = possible_operator[1]
                    token_list.append(possible_operator[0])
                    token = ''
                else:
                    token += line[index]
                    index += 1


            elif line[index] == '\n':
                if token != '':
                    token_list.append(token)
                index += 1
                token = ''

            elif self.is_separator(line[index]):
                if token != '':
                    token_list.append(token)
                token_list.append(line[index])
                index += 1
                token = ''
            else:
                token += line[index]
                index += 1

        if token != '':
            token_list.append(token)

        return token_list

    def get_operator_token(self, line, position):
        token = ''
        start = position
        while position < len(line) and self.is_part_of_operator(position):
            token += line[position]
            position += 1

        return (token, position) if self.is_operator(token) else (None, start)

    def is_part_of_operator(self, part):
        for operator in self._tokens.get_operators():
            if operator.find(str(part)) != -1:
                return True
        return False

    def is_operator(self, token):
        return token in self._tokens.get_operators()

    def is_separator(self, char):
        return char in self._tokens.get_separators()

    def is_reserved_word(self, char):
        return char in self._tokens.get_reserved_words()

    def is_identifier(self, token):
        return self.fa_identifier.check_wrapper(sequence=token)

    def is_constant(self, token):
        # return self.fa_constant.check_wrapper(sequence=token)
        return re.match(r'^(0|[+\-]?[1-9][0-9]*)$|^\'.\'$|DADADA|NAH|\'[0-9a-zA-Z][=\-!@#=$%^&*()_+{}|":\[\]<>/\\]\'$',
                        token) is not None
