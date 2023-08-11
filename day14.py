""" Solution for Day 14 """

from advent import Advent, Runner, file_to_string


class Reindeer:
    """ Class to simulate a single reindeer """

    def __init__(self, name, speed, fly_time, rest_time):
        self._name = name
        self._speed = speed
        self._fly_time = fly_time
        self._rest_time = rest_time
        self._state = None
        self._timer = 0
        self._points = 0
        self.velocity = 0
        self.distance = 0

    def __str__(self):
        return self._name

    def start(self):
        """ start a new reindeer """
        self._state = 'fly'
        self._timer = self._fly_time
        self._points = 0
        self.velocity = self._speed
        self.distance = 0

    def tick(self):
        """ next time tick for this reindeer """
        if self._state == 'fly':
            self.distance += self.velocity
        self._timer -= 1
        if self._timer == 0:
            if self._state == 'fly':
                # time to rest
                self._state = 'rest'
                self.velocity = 0
                self._timer = self._rest_time
            elif self._state == 'rest':
                # time to fly again
                self._state = 'fly'
                self.velocity = self._speed
                self._timer = self._fly_time

    def award_point(self):
        """ award a point for this reindeer """
        self._points += 1

    def get_points(self):
        """ return the current points of this reindeer """
        return self._points


class Day14(Advent):
    """ class for Day 14 solution """

    def __init__(self, input_text):
        super().__init__()
        self.name = "14"
        self.lines = input_text
        self.race = []

    def parse(self):
        for line in self.lines:
            tmp = line.strip().replace('.', '')
            words = tmp.split()
            name, speed, fly_time, rest_time = words[0], int(
                words[3]), int(words[6]), int(words[13])
            reindeer = Reindeer(name, speed, fly_time, rest_time)
            self.race.append(reindeer)

    def run_race_old(self, time_limit):
        """ run a race the old way """
        for reindeer in self.race:
            reindeer.start()

        for seconds in range(time_limit):
            _ = seconds
            for reindeer in self.race:
                reindeer.tick()
        max_distance = max([r.distance for r in self.race])
        return max_distance

    def part_one(self):
        winner = self.run_race_old(2504)
        print(f"Final: Winner has travelled {winner}")
        return winner

    def run_race_new(self, time_limit):
        """ run a race the new way """
        for reindeer in self.race:
            reindeer.start()

        for seconds in range(time_limit):
            _ = seconds
            for reindeer in self.race:
                reindeer.tick()

            max_flown = max([r.distance for r in self.race])
            for reindeer in self.race:
                if reindeer.distance == max_flown:
                    reindeer.award_point()

        max_points = max([r.get_points() for r in self.race])
        return max_points

    def part_two(self):
        winner = self.run_race_new(2504)
        print(f"Final: Winner has {winner} points")
        return winner


def main():
    """ stub for main() """
    aoc1 = Day14(file_to_string("day14-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
