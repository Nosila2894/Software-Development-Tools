class EngineClock(object):
    def __init__(self):
        self._time = 0

    def get_time(self):
        return self._time

    def update(self, delta_time):
        self._time += delta_time

