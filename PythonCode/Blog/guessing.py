import random as rand
from math import ceil
from numpy import std

# Define global variables
RANGE_MAX = 1000
RANGE_MIN = 1
NORM = RANGE_MAX - RANGE_MIN + 1
SECRET = int(round(rand.uniform(RANGE_MAX, RANGE_MIN)))


def check(number):
    if number == SECRET:
        return True
    elif number > SECRET:
        return "big"
    elif number < SECRET:
        return "small"


def test_fun(fun, times=100_000, **kwargs):
    print(f"Testing {fun.__name__} {times} times.")
    global SECRET
    SECRET = int(round(rand.uniform(RANGE_MAX, RANGE_MIN)))
    i = 1
    results_list = [fun(**kwargs)]
    while i <= times:
        SECRET = int(round(rand.uniform(RANGE_MAX, RANGE_MIN)))
        result = fun(**kwargs)
        results_list.append(result)
        i += 1
    average = sum(results_list) / times
    return (average, std(results_list))


def brute_solve():
    i = RANGE_MIN
    loop = 1
    while True:
        if check(i) is True:
            return loop
        i += 1
        loop += 1


def random_solve():
    loop = 1
    while True:
        test = int(round(rand.uniform(RANGE_MAX, RANGE_MIN)))
        if check(test) is True:
            return loop
        loop += 1


def random_once_solve():
    loop = 1
    possibilities = list(range(RANGE_MIN, RANGE_MAX + 1))
    while True:
        test = rand.choice(possibilities)
        if check(test) is True:
            return loop
        else:
            possibilities.remove(test)
        loop += 1


def intel_random_solve():
    max = RANGE_MAX
    min = RANGE_MIN
    loop = 1
    while True:
        test = round(rand.uniform(max, min))
        outcome = check(test)
        if outcome is True:
            return loop
        elif outcome == "big":
            max = test
        elif outcome == "small":
            min = test
        loop += 1


def sampling_solve(nr_samples=4):
    samples = []
    possible = list(range(RANGE_MIN, RANGE_MAX))
    spots = len(possible) / nr_samples
    loop = 1
    i = 0
    while i < nr_samples:
        try:
            samples.append(int(round(spots)))
        except IndexError:
            break
        spots += spots
        i += 1
    max = RANGE_MAX
    min = RANGE_MIN
    for item in samples:
        outcome = check(item)
        if outcome is True:
            return loop
        elif outcome == "small":
            min = item
        elif outcome == "big":
            max = item
        loop += 1
    while True:
        test = rand.uniform(max, min)
        outcome = check(test)
        if outcome is True:
            return loop
        elif outcome == "big":
            max = test
        elif outcome == "small":
            min = test
        loop += 1


def half_solve():
    max = RANGE_MAX
    min = RANGE_MIN
    diff = max - min
    test = max
    loop = 1
    while True:
        outcome = check(test)
        if outcome is True:
            return loop
        elif outcome == "big":
            max = test
            diff = max - min
            test -= ceil(diff / 2)
        elif outcome == "small":
            min = test
            diff = max - min
            test += ceil(diff / 2)
        loop += 1


def half_solve_2():
    max = RANGE_MAX
    min = RANGE_MIN
    diff = max - min
    test = round(rand.uniform(max, min))
    loop = 1
    while True:
        outcome = check(test)
        if outcome is True:
            return loop
        elif outcome == "big":
            max = test
            diff = max - min
            test -= ceil(diff / 2)
        elif outcome == "small":
            min = test
            diff = max - min
            test += ceil(diff / 2)
        loop += 1


brute_results = test_fun(brute_solve)
print("Tries took for brute forcing: " +
      str(round(brute_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(brute_results[1] / NORM, 2)) + " %")

random_results = test_fun(random_solve)
print("Tries took for random guesses: " +
      str(round(random_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(random_results[1] / NORM, 2)) + " %")

random_once_results = test_fun(random_once_solve)
print("Tries took for random guesses without reintroduction: " +
      str(round(random_once_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(random_once_results[1] / NORM, 2)) + " %")

intel_random_results = test_fun(intel_random_solve)
print("Tries took for intelligent random: " +
      str(round(intel_random_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(intel_random_results[1] / NORM, 2)) + " %")

sampling_4_results = test_fun(sampling_solve, nr_samples=4)
print("Tries took for sampling with 4 samples: " +
      str(round(sampling_4_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(sampling_4_results[1] / NORM, 2)) + " %")

sampling_10_results = test_fun(sampling_solve, nr_samples=10)
print("Tries took for sampling with 10 samples: " +
      str(round(sampling_10_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(sampling_10_results[1] / NORM, 2)) + " %")

sampling_50_results = test_fun(sampling_solve, nr_samples=50)
print("Tries took for sampling with 50 samples: " +
      str(round(sampling_50_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(sampling_50_results[1] / NORM, 2)) + " %")

sampling_100_results = test_fun(sampling_solve, nr_samples=100)
print("Tries took for sampling with 100 samples: " +
      str(round(sampling_100_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(sampling_100_results[1] / NORM, 2)) + " %")

half_results = test_fun(half_solve)
print("Tries took for halving solve: " +
      str(round(half_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(half_results[1] / NORM, 2)) + " %")

half_2_results = test_fun(half_solve_2)
print("Tries took for halving solve with random start: " +
      str(round(half_2_results[0] / NORM * 100, 2)) +
      " % of all possible numbers with standard deviation of " +
      str(round(half_2_results[1] / NORM, 2)) + " %")
