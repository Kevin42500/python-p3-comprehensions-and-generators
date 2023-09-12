# lib/list_comprehension.py

def return_evens(seq):
    return [x for x in seq if x % 2 == 0]

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]
