from automata.pda.npda import NPDA


def q3a() -> NPDA:
    return NPDA(
        states=set(),
        stack_symbols=set(),
        transitions=dict(),
        initial_state="",
        initial_stack_symbol="",
        final_states=set(),
    )


def q3b() -> list[tuple[str, list[str]]]:
    return
