#!/usr/bin/python3

import sys


def tar_mapper():
    """ This mapper select categories and return the corresponding information to category, which is video_id and country.
        Input format: csv is a data file separated by commas
        """
    for line in sys.stdin:
        # Clean input and split it with ','
        parts = line.strip().split(',')

        # Check that the line is of the correct format
        # If line is malformed, we ignore the line and continue to the next line
        if len(parts) != 12:
          continue

        # According to the data, the first column is video_id, the fourth column is category, the twentieth column is country.
        video_id = parts[0].strip()
        category = parts[3].strip()
        country = parts[11].strip()

        # In this mapper output, the key is category, the value is video_id and country
        # Output format: category \t video_id, country
        print("{}\t{},{}".format(category, video_id, country))

if __name__ == '__main__':
    tar_mapper()
