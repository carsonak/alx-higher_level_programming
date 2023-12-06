#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key holding the greatest value in a dictionary"""

    if a_dictionary:
        sotd_kys = sorted(a_dictionary.keys())
        best = [sotd_kys[0], a_dictionary[sotd_kys[0]]]

        for a_key in sotd_kys:
            if a_dictionary[a_key] > best[1]:
                best = [a_key, a_dictionary[a_key]]
    else:
        return None

    return best[0]
