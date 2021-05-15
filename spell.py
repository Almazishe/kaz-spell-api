import json
from typing import List

from symspellpy import SymSpell as SymSpellPy, Verbosity

import schemas




def create_dictionary(file) -> SymSpellPy:
    symspell = SymSpellPy()

    with open(file, encoding="utf8") as dictionary:
        symspell.create_dictionary(dictionary)

    return symspell


def SymSpell() -> SymSpellPy:
    symspell = SymSpellPy()

    symspell.load_dictionary('data/dictionary.txt', 0, 1)

    return symspell


def get_suggestions(word: str, verbosity: int) -> List[schemas.Suggestion]:
    sym_spell = SymSpell()
    suggestions = sym_spell.lookup(word, verbosity,
                               max_edit_distance=2)

    res = []
    for s in suggestions:
        suggestion = schemas.Suggestion(
            term = s.term,
            distance = s.distance,
            count = s.count
        )
        res.append(suggestion)

    return res

