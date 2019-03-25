import chone as ch1
import numpy as np

# MAYBE WE DONT NEED NUMPY? Just use a list of strings??
strings = np.array([
                   list("CCATCAACCTGTACGGGAACTTTCTATATCGTTCATACGGTTAGAGATAA"),
                   list("CCATCAACCTGTACGGGAAGGCCTTATATCGTTCTCGGACGGAGAGATAA"),
                   list("CCTTGTGAACCCCTTACCCTATTGAGGCATTGACTGATGCGGAAGGAGAT"),
                   list("CTGGAATGAACTGGTCTATGTGACAGAAACGGTTAAAGTACCTAATCTCG"),
                   list("TTAGTGTAGGTTCTGACCAATCCCTAATTCGTTGAGAACTCACAATTTTA"),
                   list("CAACTGGGGACATAAGCCCTACGCCCATCATCTACTGACGTATACCCTAT"),
                   list("TGCAGTTCAAGGCCCTTGACAGTATCCGCCGCAAGTTCTAGTGCAATGGC"),
                   list("GGTATAGTACGCTCGTAAGACCCTATAGGCGACACGGGTGGGATCATCAC"),
                   list("AAACGGTTTTACTGGGAAGACTCACAGGCCTCCGCCTATAGGCGGTGCTT"),
                   list("ACTCAAACCTCTTGCGGCTGTTAGTATTACCCCGCGAGGATTCGAAAAGG")])

# Implanted motif: "AAACCCTTT", but contains mutations in its sequence, so it
# never actually appears in the strings.
# How do we find this implanted motif into these strings? This is the motif
# finding problem.

# If we just concatenate the strings and search for a frequent pattern, we will
# never find it as the consensus never actually appears into it. Since the
# number of mutation is not constant, motif finding with mismatches will also
# fail.

# We will actually search for k-meres in each t string, construct a t x k
# motif matrix, and then score each column by finding the most common
# nucleotide and counting every mismatch. If we get a tie, we break it
# randomly. The sum of the scores of each column is score(motifs).

# Let's make some random motifs and calculate the score for each:

motifs = np.array([
    list("AAACCCTTT"),
    list("AATCCGTTA"),
    list("TTACCGTTT"),
    list("ATACCCTTC")
])


def countnucl(pattern, out=False):
    import warnings
    import operator
    """Return the most common nucleotide in the string.
    Ties are solved by looking at the order nucleotides are added to the
    dictionary, so it is more or less random.

    Variables:

    pattern -- The pattern to count nucleotides of.
    out -- Type of output:
        * False -> Returns most frequent nucleotide omitting its count.
        * True  -> Returns most frequent nucleotide including its count.
        * All   -> Returns all nucleotide counts as a nucleotide: count
                   dictionary.
        * Count -> Return only the count of the most frequent nucleotide.
        Defaults to False.
    """
    # Input handling
    if out is str:
        out = out.lower()
    elif out is bool:
        pass
    else:
        raise ValueError

    # The freq array follows A C G T.
    frequency = {}

    for letter in pattern:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    if out is True:
        return max(frequency.items(), key=operator.itemgetter(1))
    elif out is False:
        return max(frequency.items(), key=operator.itemgetter(1))[0]
    elif out == "all":  # I'm referring to this
        return frequency
    elif out == "count":
        return max(frequency.items(), key=operator.itemgetter(1))[1]
    else:
        warnings.warn("Unrecognized Out parameter! Defaulting to False.")
        return max(frequency.items(), key=operator.itemgetter(1))[0]


countnucl("AAAATTTGGG")
countnucl("ATTTTTCCGG")
countnucl("TAAATTCCGG")  # This has a tie
countnucl("ATTAATCCGG", "all")  # This has a tie
countnucl("AAAATTCCGG", True)
countnucl("ATTTTTCCGG", True)
countnucl("AAAATTCCGG", "All")
countnucl("AAAATTCCGG", "Count")


def score(motifs):
    """Score a collection of motifs in a numpy matrix."""
    # Implement an error if all strings are not of the same length??
    score = 0
    for a in range(0, len(motifs[0])):
        # For each column (here I use the length of the first line to determine
        # the column number):
        # Extract the corresponding column,
        col = "".join(motifs[:, a])

        # For each column we calculate the score and add it all together.
        score += len(motifs) - countnucl(col, "Count")

    return score


score(motifs)


def consensus(motif):
    """Return the consensus made of the most frequent nucleotide for each
    column of a motif matrix. See countnucl()"""
    result = ""
    for a in range(0, len(motifs[0])):
        col = "".join(motifs[:, a])
        result += countnucl(col)

    return result


consensus(motifs)

# Now that we found a way to score each motif, we will just need to find a
# collection of k-mere motifs from the strings, and select the collections
# that minimize score(motifs).
# We could generate each possible motif matrix and check them, but that would
# have a running time of O(L-k+1)^n.

# To devise a more efficient motif finding algorithm, we notice that we can
# compute score(motif) if we know consensus(motifs) by counting the different
# nucleotides in each row instead of in each column.
# We define dist(Pattern, Motifs) as the sum of the hemming distances between
# the pattern Pattern and each Motif in Motifs.


def dist(pattern, motifs):
    result = 0
    for a in range(0, len(motifs)):
        row = "".join(motifs[a])
        result += ch1.hamming_distance(pattern, row)

    return result


dist('AAACCCTTT', motifs)

# So, score(motifs) = dist(consensus(motifs), motifs).

dist(consensus(motifs), motifs)

# This means that we can formulate an equal problem to the motif finding one
# by simply searching for /potential/ k-mere consensus patterns that minimize
# d(Pattern, motifs) with motifs a collection of k-meres, once for each string
# of DNA.

# It would seem that the problem just got harder: instead of searching in each
# motif collection we now have to search in each motif collection each k-mere
# pattern! However,
