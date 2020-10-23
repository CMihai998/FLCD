class Tokens:
    def __init__(self):
        self._separators = []
        self._operators = []
        self._reserved_words = []

        self.initialize()

    def initialize(self):
        with open("scanner/Token.txt") as tokens_file:
            for index, line in enumerate(tokens_file):
                line = line.strip()
                if index < 15:
                    self._operators.append(line)
                elif index < 24:
                    if line == "<space>":
                        self._separators.append(" ")
                    else:
                        self._separators.append(line)
                else:
                    self._reserved_words.append(line)

    def get_separators(self):
        return self._separators

    def get_operators(self):
        return self._operators

    def get_reserved_words(self):
        return self._reserved_words

    def __str__(self):
        return "Separators: " + self._separators.__str__() + '\n' + \
               "Operators: " + self._operators.__str__() + '\n' + \
               'Reserved words: ' + self._reserved_words.__str__()
