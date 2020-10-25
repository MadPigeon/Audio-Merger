import heapq
import os
from queue import Queue


class HeapElement:
    def __init__(self, directory, files_in_directory, total_files_count):
        self.directory = directory
        self.count = files_in_directory
        self.frequency = total_files_count / files_in_directory
        self.priority = self.frequency / 2

    def produce(self):
        self.count -= 1
        self.priority += self.frequency
        return self.directory.get()

    def __lt__(self, other):
        return self.priority < other.priority

    def __len__(self):
        return self.count

    def __str__(self):
        return str(self.directory)

    def __repr__(self):
        return '(' + str(self.directory) + ', ' + str(self.count) + ')'


files = os.listdir('D:/MadPigeon/Desktop/files_to_merge')

for file in files:
    print(file)

# aha = Queue()
# a = test_class('A', 4, 8)
# b = test_class('B', 3, 8)
# c = test_class('C', 1, 8)
#
# H = [a, b, c]
# print(H)
#
# heapq.heapify(H)
#
# result = []
#
# while len(H) > 0:
#    item = heapq.heappop(H)
#    result.append(item.produce())
#    if len(item) > 0:
#        heapq.heappush(H, item)
#
# print(result)
