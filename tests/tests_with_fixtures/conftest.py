import pytest
import random



def fixture_generate_random_numbers(N=10, A=0, B=10, seed=None):
    """
    Generate N random numbers between A and B (inclusive).
    
    Args:
    N (int): The number of random numbers to generate.
    A (int): The lower bound of the random numbers.
    B (int): The upper bound of the random numbers.
    seed (int): Optional. The random seed to use for reproducibility.
    
    Returns:
    list: A list containing N random numbers.
    """
    if seed is not None:
        random.seed(seed)
    return [random.randint(A, B) for _ in range(N)]


@pytest.fixture(autouse=True)
def seed_rand_numlist():
    return fixture_generate_random_numbers(10, 0, 10, seed=None)

@pytest.fixture(autouse=True)
def seed_69105_numlist():
    return fixture_generate_random_numbers(10, 0, 10, seed=69105)

    

@pytest.fixture(autouse=True)
def number_list():
    return fixture_generate_random_numbers(10, 0, 10, seed=69105)


