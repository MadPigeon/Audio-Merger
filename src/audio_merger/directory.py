import os


class Directory:
    def __init__(self, path):
        if len(path) == 0:
            raise ValueError('The path must not be empty', path)
        if not os.path.isdir(path):
            raise TypeError('Path provided is not a directory', path)
        self.name = os.path.basename(path)
