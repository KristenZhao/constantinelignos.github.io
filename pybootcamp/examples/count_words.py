#!/usr/bin/env python
"""Create a wordlist from multiple files."""

import sys
from collections import Counter


def get_tokens(filenames):
    """Return a list of all tokens in the specified files."""
    return [token for  filename in filenames
            for line in open(filename, "U")
            for token in line.split()]


# A more efficient way to implement get_tokens using a generator
def gen_tokens(filenames):
    """Generate tokens from each file."""
    for filename in filenames:
        input_file = open(filename, "U")
        for line in input_file:
            for token in line.split():
                yield token


def count_words():
    """Parse arguments and do the work."""
    filenames = sys.argv[1:]
    tokens = get_tokens(filenames)
    word_freqs = Counter(tokens)
    for word, count in word_freqs.most_common(10):
        print(count, word)


if __name__ == "__main__":
    count_words()
