from pokerlottery import compute_winner


def test_memorized_values():
    test_array = [
        {'name': 'Alice', 'lucky_word': 'apple', 'chip_count': 1},
        {'name': 'Bob', 'lucky_word': 'banana', 'chip_count': 2},
        {'name': 'Charlie', 'lucky_word': 'cherry', 'chip_count': 3},
    ]
    assert compute_winner.compute_winner(test_array) == 'Alice'


def test_distribution():
    raise NotImplementedError("Test not implemented")
