mytext = ("""
AATGCTGAAAGACCCGGACTAGAGTGGCGAGATCTATGGCGTGTGACCCGTTATGCTCCATTTCGGTCAGTGGGT
CACAGCTAGTTGTGGATTGGATTGCCATTCTCCGAGTGTTTTAGCGTGACAGCCGCAGGGATCCCATAAAATGCA
ATCGTAGTCCACCTGATCGTACTTAGAAATGAGGGTCCGCTTTTGCCCACGCACCTGATCGCTCCTCGTTTGCTT
TTAAGAACCGGACGAACCACAGAGCATAAGGAGAACCTCTAGCTGCTTTACAAAGTACTGGTTCCCTTTCCAGCG
GGATGCTTTATCTAAACGCAATGAGAGAGGTATTCCTCAGGCCACATCGCTTCCTAGTTCCGCTGGGATCCATCG
TTGGCGGCCGAAGCCGCCTATAATAGTGAGTATAACGTCTGTTATAACTGTGCCAGATCGTCTATAACAAATAGC
CGATCCAGTTTATCTCTCGAAACTATAGTCGTACAGATCGAAATCTTAAGTCAAATCACGCGACTAGACTCAGCT
CTATTTTAGTGGTCATGGGTTTTGGTCCCCCCGAGCGGTGCAACCGATTAGGACCATGTAGAACATTAGTTATAA
GTCTTCTTTTAAACACAATCTTCCTGCTCAGTGGTACATGGTTATCGTTATTGCTAGCCAGCCTGATAAGTAACA
CCACCACTGCGACCCTAATGCGCCCTTTCCACGAACACAGGGCTGTCCGATCCTATATTACGACTCCGGGAAGGG
GTTCGCAAGTCGCACCCTAAACGATGTTGAAGGCTCAGGATGTACACGCACTAGTACAATACATACGTGTTCCGG
CTCTTATCCTGCATCGGAAGCTCAATCATGCATCGCACCAGCGTGTTCGTGTCATCTAGGAGGGGCGCGTAGGAT
AAATAATTCAATTAAGATATCGTTATGCTAGTATACGCCTACCCGTCACCGGCCAACAGTGTGCAGATGGCGCCA
CGAGTTACTGGCCCTGATTTCTCCG""".replace("\n", ""))

# Pattern Count Problem
# Given a text and a pattern, return the number of occurrences of pattern
# in text.


def pattern_count(text, pattern):
    """Count the reoccurence of pattern in text."""
    count = 0
    for i in range(0, len(text) - len(pattern)):
        # Slide a window of len(pattern) to search for pattern in the text.
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count


# Frequent Words problem:
# Input: a string Text and an integer k.
# Output: All most frequent k-meres in Text.


def frequent_words(text, k):
    """Find the most freqnt k-mere in a string."""
    result = set()  # Using a set to remove duplicates from the result
    count = []
    for i in range(0, len(text) - k):
        # Slide the window and count the occurrences of each slice.
        pattern = text[i: i + k]
        count.append(pattern_count(text, pattern))
    for i in range(0, len(text) - k):
        # Scan the count list to search for all the k-meres with the most
        # occurrences.
        if count[i] == max(count):
            result.add((text[i: i+k], count[i]))
    return result


# We wish to make the frequent_words algorithm faster by removing the
# necessity for it to scan the text for each k-mere in the sequence.
# We will do this by only scanning the text once, then noting down each
# occurrence of pattern in the text.
#
# We will need to generate an array containing all possible combinations of
# k-meres in the text, but we can avoid this by encoding each pattern as a
# number, treating this number as an index position, and then adding one to
# the corresponding position for each number found.
# How do we encode a pattern to a number?
#
# Pattern to number and Number to Pattern
# In an ordered frequency array, convert a pattern to its index number, and
# an index number plus the length k to a pattern.

# First we need to encode each nucleotide to a number.


def sym_to_num(a):
    """Encode a nucleotide to a number.

    A -> 0; C -> 1; G -> 2; T -> 3"""
    if a == "A" or a == "a":
        return 0
    if a == "C" or a == "c":
        return 1
    if a == "G" or a == "g":
        return 2
    if a == "T" or a == "t":
        return 3


def num_to_sym(a):
    """Decode a number to a nucleotide.

    0 -> A, 1 -> C, 2 -> G, 3 -> T"""
    return ["A", "C", "G", "T"][a]

# To encode a pattern into a number, we consider that by ordering all k-meres
# in lexicographic order, when we remove the last letter from each k-mere
# we obtain (k-1)-meres repeated four times each. By using this characteristic,
# we can convert a pattern to a number by removing the last nucleotide,
# converting it into a number, and multiplying by four the pattern to number
# result of the remainder of the pattern.


def pattern_to_number(pattern):
    """Encode a nucleotide pattern to a number."""
    # End the reoccurring call if pattern is empty.
    if pattern == "":
        return 0
    # Remove the last symbol of the pattern, evaluate it, and code it into a
    # number.
    last_symbol = pattern[len(pattern) - 1]
    prefix = pattern[0: len(pattern) - 1]

    # Return four times the encoding of the rest of the pattern plus the
    # encoding of the last nucleotide. This is done recursively.
    return 4 * pattern_to_number(prefix) + sym_to_num(last_symbol)


# Similarly, we can decode the number into a pattern by recovering the last
# number added (by % 4), decoding it into a nucleotide, the dividing the number
# by 4 and repeating the algorithm k number of times.


def number_to_pattern(index, k):
    """Decode a number to a nucleotide pattern."""
    # End the recursive call
    if k == 1:
        return num_to_sym(index)

    prefindex = index // 4  # Find the number associated with the prefix
    rem = index % 4         # Find the number associated with the last letter
    sym = num_to_sym(rem)   # Decode the last letter

    # Decode the rest of the prefix
    prefixpattern = number_to_pattern(prefindex, k - 1)
    # Concatenate the result of the prefix with the last nucleotide.
    return prefixpattern + sym


# We now slide a window down the text, and keep count of each pattern's
# frequency by storing its frequency such that frequency[i] is the
# frequency of the pattern number_to_pattern(i).


def compute_frequencies(text, k):
    """Create a frequency array for nucleotides.

    This is done by sliding a window down text, encoding each slice to a
    number, and adding 1 to the corresponding position in the array. The
    frequency array contains the counts of all possible k-meres.
    """
    # Initialize an empty frequency array
    frequencies = [0] * (4 ** k)
    # Slide the window, and encode each pattern in the frequency array.
    for i in range(0, len(text) - k + 1):
        pattern = text[i: i + k]
        a = pattern_to_number(pattern)
        frequencies[a] += 1
    return frequencies

# To find the most frequent pattern, we just look where the frequency array
# is higher and decode that number's index into a pattern.


def better_frequent_words(text, k, givefreq=False):
    """Find the most frequen k-mere in text.

    More efficient than frequent_words. Uses the generation of a frequency
    array to return most-occurring k-meres in text.
    """
    result = set()  # To remove doubles.
    frequencies = compute_frequencies(text, k)
    maxfreq = max(frequencies)

    # Scan the frequency array for its maximum values and decode their indexes.
    for i in range(0, (4 ** k - 1)):
        if frequencies[i] == maxfreq:
            pattern = number_to_pattern(i, k)
            result.add(pattern)
    if givefreq is False:
        return result
    else:
        return [result, maxfreq]


# better_frequent_words(mytext, 6) Has an execution of about 0.005 seconds.
# frequent_words(mytext, 6)        Has an execution of about 0.196 seconds.

# Reverse pattern problem:
# Input: A DNA string Pattern.
# Output: the reverse complement of Pattern.

# First, we need to make a basic function to give nucleotide complementaries:


def base_compl(a):
    """Given a nucleotide, return its complementary."""
    if a == "A" or a == "a":
        return "T"
    if a == "C" or a == "c":
        return "G"
    if a == "G" or a == "g":
        return "C"
    if a == "T" or a == "t":
        return "A"


def reverse_DNA(Pattern):
    """Give the reverse complementary of a DNA string"""
    result = ""
    for i in reversed(Pattern):
        result += base_compl(i)
    return result


# Clump-finding problem:
# Input: A string genome, an the integers k, L and t.
# Output: All distinct k-meres forming L, t clumps, meaning they are found
# t times in an L window in the genome.

# We can solve this problem inefficiently by repeated use of the
# better_frequent_words function.


def bad_clump_finding(genome, k, t, l):
    """A slow way to find l, t clumps of k-meres in the genome.

    Variables:

    genome -- The genome in which to search for clumps.
    k -- The length of the pattern.
    t -- The minimum times that a k-length pattern has to occur in the window
         to be considered a clump.
    l -- The length of the window where the k-mere has to repeat a t number of
         times to be considered a clump.
    """
    # Variable initialization
    frequent_patterns = set()
    clump = [0] * (4 ** k)

    # Slide a window sized l down the genome and compute frequencies for each.
    for i in range(0, len(genome) - l):
        text = genome[i: i + l]
        frequencies = compute_frequencies(text, k)
        # If there are any k-meres that are present more than t times in the
        # window, mark it as forming a clump.
        for i in range(0, 4 ** k - 1):
            if frequencies[i] >= t:
                clump[i] = 1
    # Decode the clump-forming sequences and return them.
    for i in range(0, 4 ** k - 1):
        if clump[i] == 1:
            frequent_patterns.add(number_to_pattern(i, k))

    return frequent_patterns

# To speed up the clump finding algorithm, we can notice that when we slide our
# window down the genome, the frequency array changes in only two positions:
# the starting k-mere of the old text is reduced by one,
# the ending k-mere of the new sequence is increased by one.
#
# By not generating a new array for each window but simply changing the old
# one, we can speed up the algorithm significantly:


def clump_finding(genome, k, t, l):
    """Find l, t clumps of k-meres in the genome.

    Better than bad_clump_finding.

    Variables:

    genome -- The genome in which to search for clumps.
    k -- The length of the pattern.
    t -- The minimum times that a k-length pattern has to occur in the window
         to be considered a clump.
    l -- The length of the window where the k-mere has to repeat a t number of
         times to be considered a clump.
    """
    # Variable initialization
    frequent_patterns = set()
    clump = [0] * (4 ** k)
    text = genome[0: l]

    # Compute frequencies for the first window
    freqs = compute_frequencies(text, k)
    # Find clumps in the first window
    for i in range(0, 4 ** k - 1):
        if freqs[i] >= t:
            clump[i] = 1

    # Modify the old frequency array
    for i in range(1, len(genome) - l):
        # From 1 as the first window has already been computed.

        # Find the first and last pattern indexes.
        firstpattern = genome[i - 1: i + k - 1]
        lastpattern = genome[i + l - k: i + l]
        firstindex = pattern_to_number(firstpattern)
        lastindex = pattern_to_number(lastpattern)

        # Update the frequencies of the first and last accordingly.
        freqs[firstindex] -= 1  # The first pattern exits
        freqs[lastindex] += 1   # The last pattern enters

        if freqs[lastindex] >= t:  # Find if any pattern forms clumps
            clump[lastindex] = 1
    # Decode the clump-forming sequences and return them.
    for i in range(0, 4 ** k - 1):
        if clump[i] == 1:
            frequent_patterns.add(number_to_pattern(i, k))

    return frequent_patterns


# bad_clump_finding(mytext, 5, 4, 50) takes about 0.25 seconds
# clump_finding(mytext, 5, 4, 50)     takes about 0.008 seconds

# Hamming distance
# Input: Two strings of equal length
# Output: The Hamming distance between them


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

# Aproximate pattern finding algorithm:


def aprox_pattern_count(text, pattern, d):
    count = 0

    for i in range(0, len(text) - len(pattern)):
        # Slide a window of len(pattern) to search for pattern in the text
        # include the pattern only if it differs from the query pattern
        # a maximum of d.
        if hamming_distance(text[i: i + len(pattern)], pattern) < d:
            count += 1
    return count


# We now take the next step and find all k-meres that are found in the text,
# and return all occurrences of these pattern plus of all patterns that have
# a maximum hemming distance of d.
#
# We could generate all possible k-meres with less than d of hemming distance,
# but this will be very inefficient, as many of the generated k-meres will
# never show up in the text.
# So, we wish to create an algorithm that only checks k-meres that are close
# to the pattern, or their neighbours.
# pattern' is a neighbour of pattern if its hemming distance is d at maximum.

# First, we can generate all neighbours of hemming distance = 1:


def immediate_neighbours(pattern):
    """Return each neighbour of pattern with hemming distance 1."""
    neighbours = set()
    neighbours.add(pattern)  # The first pattern is a neighbour of itself.
    symbols = set(["A", "C", "T", "G"])  # Used to change the letter later.

    for i in range(0, len(pattern)):  # For each letter in the pattern
        modpattern = list(pattern)    # A list is mutable
        last_symbol = pattern[i]
        # Change a letter at a time with every other letter (except itself).
        for element in symbols - set(last_symbol):
            modpattern[i] = element
            neighbours.add("".join(modpattern))

    return neighbours


def neighbours(pattern, d):
    """Find all neighbours of pattern with at maximum d differences."""
    # End the recursive call
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return set(["A", "C", "G", "T"])
    # Initalize some varibles.
    nucleotides = set(["A", "C", "G", "T"])
    result = set()
    # Search for neighbours of the suffix (pattern minus the last letter)
    suffixneighbours = neighbours(pattern[0: len(pattern) - 1], d)

    # For each neighbour in the suffix, if its hamming distance is less than
    # d, produce all combinations by adding different last nucleotides.
    for item in suffixneighbours:
        if hamming_distance(pattern[0: len(pattern) - 1], item) < d:
            for nucleotide in nucleotides:
                result.add(nucleotide + item)
        else:
            result.add(pattern[0] + item)
    return result


def freq_words_mis(text, k, d):
    """Find most frequent k-meres with at most d mismatches.

    Variables:
    text -- Where to search for k-meres.
    k -- lenght of each k-mere.
    d -- maximum number of mismatches in each k-mere."""

    # Initalize variables
    result = set()
    close = [0] * (4 ** k)
    frequencies = [0] * (4 ** k)

    # slide a window down the text, and generate neighbours, encoding them
    # in a frequency array "close". This way, we don't consider useless
    # neighbours.
    for i in range(0, len(text) - k):
        neighborhood = neighbours(text[i: i + k], d)
        for item in neighborhood:
            index = pattern_to_number(item)
            close[index] = 1
    # Knowing the neighbours, we count the occurrences of each neighbour
    for i in range(0, (4 ** k - 1)):
        if close[i] == 1:
            pattern = number_to_pattern(i, k)
            frequencies[i] = aprox_pattern_count(text, pattern, d)

    # We decode the patterns that occour with the maximum frequencies.
    maxfreq = max(frequencies)
    for i in range(0, (4 ** k - 1)):
        if frequencies[i] == maxfreq:
            pattern = number_to_pattern(i, k)
            result.add(pattern)

    return result


freq_words_mis(mytext, 5, 1)
