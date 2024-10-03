from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


def q2a() -> str:
    return "01100"


def q2b(a: DFA, b: DFA) -> NFA:

    # for each state in a
    #   create an epsilon transition to the start state in b
    #   create an epsilon transition from the accept state in b to the start state of a copy of a

    # remove the accept state of a
    # remove the accept state of b

    # can assume only one accept state for b
    additional_transitions = {state: set(b.final_states).pop() for state in a.states}

    return additional_transitions


q2b()
