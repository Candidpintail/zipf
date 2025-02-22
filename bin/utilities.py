"""Collections fo commonly used function."""

import sys
import csv


def collection_to_csv(collection, num=None):
    """
    Write out collections of items and counts in csv format.

    Parameters
    ----------
    collection : collections.Counter
        Collection of items and counts
    num : int
        Limit output to N most frequent items
    """
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    sys.stdout.reconfigure(encoding='utf-8', newline="")
    writer = csv.writer(sys.stdout)
    writer.writerows(collection[0:num])

