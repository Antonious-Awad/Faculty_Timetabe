import Connection

connection = Connection.Connection()

import Schedule


class Population:
    def __init__(self, size):
        self._size = size
        self._data = connection
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule.Schedule().initialization())

    def get_schedules(self): return self._schedules
