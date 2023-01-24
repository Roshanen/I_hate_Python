def is_plusone_dictionary(d):
    return sum(d.values()) - sum(d.keys()) == len(d) and sum(d.keys()) == len(d)*len(d)
