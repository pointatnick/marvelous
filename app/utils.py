def find_common_list(comics_lists ):
    """ returns list of common list given list of list of comics from different heros"""
    comics_sets = []
    for comics in comics_lists:
        comics_sets.append(set(comics))
    
    return set.intersection(*comics_sets)