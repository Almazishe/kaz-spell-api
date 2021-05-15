from typing import List

from fastapi import FastAPI
from symspellpy.symspellpy import Verbosity

import spell 
import schemas


app = FastAPI()




@app.get('/dictionary')
def get_dictionary():
    """
        Frequency dictionary of kazakh words

    Returns:
        dict: Frequency dictionary of kazakh words
    """
    sym_spell = spell.SymSpell()
    return sym_spell.words


@app.get('/similar/closest', response_model=List[schemas.Suggestion])
def get_closests(query: str):
    """
        Returns list of closest words

    Returns:
        suggestions List[Suggestion]: List of all suggestions, that are similar with word you entered
    """
    suggestions = spell.get_suggestions(query, Verbosity.CLOSEST)
    return suggestions


@app.get('/similar/all', response_model=List[schemas.Suggestion])
def get_closests(query: str):
    """
        Returns list of all words similar to given word

    Returns:
        suggestions List[Suggestion]: List of all suggestions, that are similar with word you entered
    """
    suggestions = spell.get_suggestions(query, Verbosity.ALL)
    return suggestions


@app.get('/similar/top', response_model=schemas.Suggestion)
def get_closests(query: str):
    """
        Returns the most similar word

    Returns:
        suggestions Suggestion: Word that is most similar to your query
    """
    suggestions = spell.get_suggestions(query, Verbosity.TOP)
    return suggestions[0]


