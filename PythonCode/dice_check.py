from pathlib import Path
from random import randint as ri
from math import floor

import pandas as pd

from tqdm import tqdm


def roll_set(dice_fun, times=1000000):
    result = []
    for _ in range(times):
        result.append(dice_fun())

    return result


def d(sides):
    return ri(1, sides)


def send_to_csv(path: str, *args):
    path = Path(path)
    columns = {}
    for function in tqdm(args):
        columns[function.__name__] = pd.DataFrame(roll_set(function))

    data = pd.concat(columns, axis=1)
    data.to_csv(path)


def main(path):
    send_to_csv(
        path,
        one_d20,
        three_d6,
        weighted_three_d6,
        weighted_d20,
        mean_d20,
        five_d4,
        two_d10,
        d10_d8,
    )


#########################################


def one_d20():
    """1 d20 per set"""
    return d(20)


def three_d6():
    """sum of 3d6"""
    return sum([d(6), d(6), d(6)])


def weighted_three_d6():
    """Remove the lesser of the D6 and then sum them"""
    a = [d(6), d(6), d(6), d(6)]
    a.sort()
    return sum(a[1:])


def weighted_d20():
    """Roll three d20 and choose the middle value"""
    a = [d(20), d(20), d(20)]
    a.sort()
    return a[1]


def mean_d20():
    """Roll three d20 and choose the mean value"""
    a = [d(20), d(20), d(20)]
    return floor(sum(a) / 3)


def five_d4():
    """Sum the roll of five d4"""
    return sum([d(4), d(4), d(4), d(4), d(4)])


def two_d10():
    return sum([d(10), d(10)])


def d10_d8():
    """Roll a d10 and a d8 then sum them"""
    return sum([d(10), d(8)])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path")

    args = parser.parse_args()

    main(args.path)
