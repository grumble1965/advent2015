from advent import Advent, Runner, file_to_string
import sys


class Reindeer:
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
        self._state = 'fly'
        self._timer = self._fly_time
        self._points = 0
        self.velocity = self._speed
        self.distance = 0

    def tick(self):
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
        self._points += 1

    def get_points(self):
        return self._points


class Day14(Advent):
    def __init__(self, input_text):
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

    def runRaceOld(self, timeLimit):
        for r in self.race:
            r.start()

        for seconds in range(timeLimit):
            for r in self.race:
                r.tick()
        maxDistance = max([r.distance for r in self.race])
        return maxDistance

    def part_one(self):
        winner = self.runRaceOld(2504)
        print(f"Final: Winner has travelled {winner}")
        return winner

    def runRaceNew(self, timeLimit):
        for r in self.race:
            r.start()

        for seconds in range(timeLimit):
            for r in self.race:
                r.tick()

            max_flown = max([r.distance for r in self.race])
            for r in self.race:
                if r.distance == max_flown:
                    r.award_point()

        maxPoints = max([r.get_points() for r in self.race])
        return maxPoints

    def part_two(self):
        winner = self.runRaceNew(2504)
        print(f"Final: Winner has {winner} points")
        return winner


def main():
    aoc1 = Day14(file_to_string("day14-live.txt"))
    runner = Runner(aoc1)
    runner.run()


if __name__ == '__main__':
    main()
