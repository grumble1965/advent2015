import sys


class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self._name = name
        self._speed = speed
        self._fly_time = fly_time
        self._rest_time = rest_time
        self._state = None
        self._timer = 0
        self.velocity = 0
        self.distance = 0

    def __str__(self):
        return self._name

    def start(self):
        self._state = 'fly'
        self._timer = self._fly_time
        self.velocity = self._speed

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


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    race = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip().replace('.', '')
            words = tmp.split()
            name, speed, fly_time, rest_time = words[0], int(words[3]), int(words[6]), int(words[13])
            # print(f"{name} = {speed} for {fly_time} then rest for {rest_time}")
            reindeer = Reindeer(name, speed, fly_time, rest_time)
            race.append(reindeer)

    print(f"{race}")
    for r in race:
        r.start()

    for seconds in range(2504):
        for r in race:
            r.tick()
        print(f"After {seconds}:  ", end='')
        for r in race:
            print(f"{r.distance} ", end='')
        print()
    print(f"Final: Winner has travelled {max([r.distance for r in race])}")


if __name__ == '__main__':
    main()