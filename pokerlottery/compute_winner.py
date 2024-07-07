import random

def compute_winner(info_array):
    """Given an array of names, lucky words, and chip counts, compute a winner"""
    # each element of the array should be a dict with a name, a lucky word, and a chip count
    if len(info_array) == 0:
        raise ValueError("Empty array passed to compute_winner")
    for info in info_array:
        # TODO in errors return the naughty element
        if 'name' not in info or 'lucky_word' not in info or 'chip_count' not in info:
            raise ValueError("Array passed to compute_winner must have name, lucky_word, and chip_count")
        if not isinstance(info['name'], str):
            raise ValueError("Name must be a string")
        if not isinstance(info['lucky_word'], str):
            raise ValueError("Lucky word must be a string")
        if not isinstance(info['chip_count'], int):
            raise ValueError("Chip count must be an int")
    # set the random seed
    info_array.sort(key=lambda x: x['name'])
    seed = ''.join([info['name'] + info['lucky_word'] + str(info['chip_count'])
                    for info in info_array])
    random.seed(seed)
    # select a random chip
    total_chips = sum([info['chip_count'] for info in info_array])
    rand_num = random.random()
    # find the winner
    winner = None
    for info in info_array:
        rand_num -= info['chip_count'] / total_chips
        if rand_num < 0:
            winner = info['name']
            break
    if winner is None:
        raise RuntimeError("No winner found")
    return winner
