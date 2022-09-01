#!/usr/bin/python3

def best_score(a_dict):
    if a_dict is None or a_dict == {}:
        return None
    maxval = max(a_dict.values())
    for key, value in a_dict.items():
        if value is maxval:
            return key
