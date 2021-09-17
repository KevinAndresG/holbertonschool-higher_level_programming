#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or a_dictionary == {}:
        return None
    v = max(a_dictionary, key=lambda k: a_dictionary.get(k))
    return v
