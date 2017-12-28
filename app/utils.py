def parse_input(input):
    characters = input.split(',')
    formatted_characters = []
    for character in characters:
        temp = character.strip()
        if temp != '':
            formatted_characters.append(temp)
    return formatted_characters


def find_common_list(comics_lists):
    # given a list of a list of comic titles,
    # returns list of titles in both sets
    comics_sets = []
    for comics in comics_lists:
        comics_sets.append(set(comics))

    return set.intersection(*comics_sets)
