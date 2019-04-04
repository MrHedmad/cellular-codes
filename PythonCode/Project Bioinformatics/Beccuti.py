# 1 - Hamming distance


def hamming_distance(a, b):
    """Give the number of nucleotide differences between two patterns."""
    # Raise an exception if a and b are of different lengths.
    if len(a) != len(b):
        raise ValueError("Lengths of two strings must be equal.")

    result = 0  # Initalize

    for i in range(0, len(a)):
        if a[i] == b[i]:
            pass
        else:
            result += 1
    return result


def DPChange(money, coin):
    import math

    minNumCoins = [0] * money
    print(len(minNumCoins))
    for m in range(1, money):
        print(minNumCoins[m])
        minNumCoins[m] = math.inf
        for i in range(0, len(coin) - 1):
            if m >= coin[i] and minNumCoins[m - coin[i]] + 1 < minNumCoins[m]:
                minNumCoins[m] = minNumCoins[m - coin[i]] + 1

    return minNumCoins[money-1]


DPChange(6, [1, 2, 6, 8])
