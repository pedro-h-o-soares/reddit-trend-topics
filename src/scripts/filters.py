import numpy as np
from ..constants.ignored import REMOVED_CHARS, IGNORED_WORDS, IGNORED_EMOJIS

def filter_characters(input: str) -> str:    
    title = ''.join(s for s in input if s not in REMOVED_CHARS and not s.isdigit()).lower()
    title = IGNORED_EMOJIS.sub(r'', title)

    return title

def filter_words(input: list[str]) -> list[str]:
    return [value for value in input if value not in IGNORED_WORDS]