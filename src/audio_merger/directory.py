import os

from src.audio_merger.file import File


class Directory:
    def __init__(self, path):
        if len(path) == 0:
            raise ValueError('The path must not be empty', path)
        if not os.path.isdir(path):
            raise TypeError('Path provided is not a directory', path)
        self.name = os.path.basename(path)

        self.files = []
        files = os.listdir(path)
        for file in files:
            self.files.append(File(os.path.join(path, file)))
