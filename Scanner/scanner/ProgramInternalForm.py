class ProgramInternalForm:
    def __init__(self):
        self._program_internal_form = []

    def add(self, token, position):
        self._program_internal_form.append((token, position))

    def __str__(self):
        return "Program Internal Form:\n\t" + self._program_internal_form.__str__()
