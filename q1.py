from automata.fa.dfa import DFA


def q1a() -> DFA:
    return DFA(
        states=set(f"q{i}" for i in range(8)),
        input_symbols={"0", "1"},
        transitions={
            "q0": {"0": "q1", "1": "q0"},
            "q1": {"0": "q2", "1": "q7"},
            "q2": {"0": "q1", "1": "q3"},
            "q3": {"0": "q4", "1": "q3"},
            "q4": {"0": "q5", "1": "q7"},
            "q5": {"0": "q4", "1": "q6"},
            "q6": {"0": "q6", "1": "q6"},
            "q7": {"0": "q7", "1": "q7"},
        },
        initial_state="q0",
        final_states={"q5", "q6"},
    )


def q1b() -> str:
    return "(0*1*)*((00)(00)*1*)(0*1*)*((00)(00)*1*)(0*1*)*"
