import json
from menu import Menu
from anytree import Node, RenderTree, find

class AutomationNode(Node):
    def __init__(self, name, parent, transition=None):
        super(AutomationNode, self).__init__(name, parent)
        self.parent = parent
        self.transition = transition
    
    def _post_detach(self, parent):
        self.transition = None


class FiniteAutomaton:
    def __init__(self, file_path):
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
                possible_future_states.append(element for element in future_state)
        if not possible_future_states:
            return False
        else:
            return any([self.check(sequence[1:], state) for state in possible_future_states])

if __name__ == '__main__':
    finite_autoamton = FiniteAutomaton("input.json")
    print(finite_autoamton.transitions)
    finite_autoamton.menu.open()
#TODO determinism