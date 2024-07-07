import random

from pokerlottery import compute_winner


def test_memorized_values():
    test_array = [
        {'name': 'Alice', 'lucky_word': 'apple', 'chip_count': 1},
        {'name': 'Bob', 'lucky_word': 'banana', 'chip_count': 2},
        {'name': 'Charlie', 'lucky_word': 'cherry', 'chip_count': 3},
    ]
    assert compute_winner.compute_winner(test_array) == 'Alice'


def test_distribution():
    num_trials = 30_000
    num_alice = 0
    num_bob = 0
    num_charlie = 0
    for i in range(num_trials):
        test_array = [
            {'name': 'Alice', 'lucky_word': 'apple', 'chip_count': 1},
            {'name': 'Bob', 'lucky_word': str(random.random()), 'chip_count': 2},
            {'name': 'Charlie', 'lucky_word': 'cherry', 'chip_count': 3},
        ]
        winner = compute_winner.compute_winner(test_array)
        if winner == 'Alice':
            num_alice += 1
        elif winner == 'Bob':
            num_bob += 1
        elif winner == 'Charlie':
            num_charlie += 1
        else:
            assert False, f"invalid winner: should be Alice, Bob, or Charlie, is {winner}"
    alice_mean = num_trials / 6.0
    bob_mean = num_trials / 3.0
    charlie_mean = num_trials / 2.0
    alice_std = ((num_trials / 6.0) * (5.0 / 6.0)) ** 0.5
    bob_std = ((num_trials / 3.0) * (2.0 / 3.0)) ** 0.5
    charlie_std = ((num_trials / 2.0) * (1.0 / 2.0)) ** 0.5
    assert abs(num_alice - alice_mean) < 3 * alice_std
    assert abs(num_bob - bob_mean) < 3 * bob_std
    assert abs(num_charlie - charlie_mean) < 3 * charlie_std
