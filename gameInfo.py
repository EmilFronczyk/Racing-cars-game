import time
class GameInfo:
    LEVELS = 10
    LAPS = 3
    def __init__(self,level=1,lap=1):
        self.level = level
        self.lap = lap
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started =False

    def next_lap(self):
        self.lap += 1

    def race_finished(self):
        return self.lap > self.LAPS

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started =True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)