from automata.pda.npda import NPDA


def q3a() -> NPDA:
    return NPDA(
        states={"q0", "q1", "q2", "q3"},
        input_symbols={"a", "b"},
        stack_symbols={"#", "X"},
        transitions={
            "q0": {
                "": {"#": {("q1", "#")}, "X": {("q1", "X")}},
                "a": {"#": {("q0", ("X", "#"))}, "X": {("q0", ("X", "X"))}},
                "b": {"#": {("q0", ("X", "#"))}, "X": {("q0", ("X", "X"))}},
            },
            "q1": {
                "a": {"#": {("q1", "")}, "X": {("q1", "")}},
                "b": {"#": {("q2", "")}, "X": {("q2", "")}},
            },
            "q2": {
                "": {"#": {("q3", "")}, "X": {("q2", "")}},
                "a": {"#": {("q2", "")}, "X": {("q2", "")}},
                "b": {"#": {("q2", "")}, "X": {("q2", "")}},
            },
        },
        initial_state="q0",
        initial_stack_symbol="#",
        final_states={"q3"},
    )


def q3b() -> list[tuple[str, list[str]]]:
    return [
        ("A", ["BC"]),
        ("B", ["a", "b", "BB"]),
        ("C", ["DbD"]),
        ("D", ["a", "b", "", "DD"]),
    ]
