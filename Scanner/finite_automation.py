import json
from menu import Menu

class FiniteAutomaton:
    def __init__(self, file_path, deterministic=False):
        with open(file_path) as file:
            data = json.load(file)
        
        self.states = data["states"]
        self.start_state = data["start_state"]
        self.final_states = data["final_states"]
        self.alphabet = data["alphabet"]
        self.transitions = data["transitions"]
        self.start_node = None
        self.menu = Menu(options=[
            ("Print states", self.__print_states),
            ("Print alphabet", self.__print_alphabet),
            ("Print final states", self.__print_final_states),
            ("Print transition dictionary", self.__print_transitions),
            ("Check sequence", self.check_wrapper),
            ("Close", Menu.CLOSE)])

        if deterministic:
            self.__deterministic = True
            new_transitions = {}
            for transition in self.transitions:
                key_list = [element[0] for element in transition[1]]
                print(key_list)
                assert len(key_list) == len(set(key_list))
                values = {}
                for element in transition[1]:
                    values[element[0]] = element[1]
                new_transitions[transition[0]] = values
            self.transitions = new_transitions


    def __print_states(self):
        print(self.states)
    
    def __print_alphabet(self):
        print(self.alphabet)

    def __print_final_states(self):
        print(self.final_states)

    def __print_transitions(self):
        print(self.transitions)
    
    def check_wrapper(self, sequence=None):
        if not sequence:
            sequence = input("Give a sequence:")
        result = self.check(sequence=sequence, current_state=self.start_state)
        return result
        if result:
            print("Valid sequence")
        else:
            print("Invalid sequence for this automaton")
    
    def check(self, sequence=None, current_state=None):
        if sequence == "":
            if current_state in self.final_states:
                return True
            else:
                return False
        
        char = sequence[0]
        possible_future_states = []
        for transition, future_state in self.transitions[current_state].items():
            if transition == char:
                possible_future_states.append(future_state)

        if not possible_future_states:
            return False
        else:
            return any([self.check(sequence[1:], state) for state in possible_future_states])

if __name__ == '__main__':
    finite_autoamton = FiniteAutomaton("input.json", deterministic=True)
    finite_autoamton.menu.open()
