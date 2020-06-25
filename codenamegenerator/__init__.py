from typing import List

import csv
import os
import random

DICT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dicts")


def dictionary_sample(name: str, sample: int = 1) -> List[str]:
    # TODO: Cache counting, and use file.seek to speed file reading.

    fname = os.path.join(DICT_DIR, f"{name}.csv")

    if not os.path.exists(fname):
        raise ValueError(f"{name} dictionary does not exists.")

    with open(fname, "rt") as csvfile:
        csvreader = csv.DictReader(
            csvfile, fieldnames=["NAME"], delimiter=",", quotechar='"'
        )

        names = [row["NAME"] for row in csvreader]

    return random.sample(names, sample)


def generate_codenames(
    prefix: str = "adjectives",
    suffix: str = "mobi_notable_scientists_and_hackers",
    num: int = 1,
) -> List[str]:
    prefixes = dictionary_sample(prefix, num)
    suffixes = dictionary_sample(suffix, num)

    return [f"{prefix} {suffix}" for prefix, suffix in zip(prefixes, suffixes)]
