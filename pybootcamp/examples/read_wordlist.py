#!/usr/bin/env python
"""Read a wordlist and print information about it."""

import sys
from collections import Counter


def load_wordlist(path):
    """Read a wordlist into a dictionary."""
    counts = {}
    for line in open(path, "U"):
        count, word = line.rstrip().split()
        counts[word] = int(count)
    return counts


def count_letters(word_counts):
    """Return letter counts from a dictionary of word counts."""
    counts = Counter()
    for word, count in word_counts.items():
        for letter in word:
            counts[letter] += count

    return counts


def read_wordlist():
    """Read a wordlist and print information about it."""
    # Check argument size
    if len(sys.argv) != 2:
        print("Usage: read_wordlist.py wordlist", file=sys.stderr)
        sys.exit(1)

    # Load up the counts
    word_counts = load_wordlist(sys.argv[1])

    # Print a sample of 10
    print("Sample:")
    for key, value in list(word_counts.items())[:10]:
        print(key, value)
    print()

    # Print the alphabetically sorted keys
    print("First ten keys:")
    for key in sorted(word_counts)[:10]:
        print(key, word_counts[key])
    print()

    # Print the letter counts
    print("Letter counts:")
    letter_counts = count_letters(word_counts)
    for letter, count in list(letter_counts.items()):
        print(letter, count)


if __name__ == "__main__":
    read_wordlist()
