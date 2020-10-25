import os
import re


class File:
    def __init__(self, path):
        if len(path) == 0:
            raise ValueError('The path must not be empty', path)
        if not os.path.isfile(path):
            raise TypeError('Path provided was not a file', path)

        self.original_full_path = path
        self.original_name = os.path.basename(path)
        self.original_directory = os.path.basename(os.path.dirname(path))

        match_groups = re.match(r"(\d+) (.+)", self.original_name).groups()
        self.original_number = int(match_groups[0])
        self.name_without_number = match_groups[1]

    def __lt__(self, other):
        if self.original_directory != other.original_directory:
            return 0
        if self.original_number < other.original_number:
            return -1
        elif self.original_number > other.original_number:
            return 1
        else:
            return 0
