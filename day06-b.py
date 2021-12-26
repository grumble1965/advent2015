import sys


lights = []


def init_lights():
    for y in range(1000):
        row = []
        for x in range(1000):
            row.append(0)
        lights.append(row)


def handle_command(command, x0, y0, xn, yn):
    dy = yn - y0
    ystep = 1 if dy > 0 else -1

    dx = xn - x0
    xstep = 1 if dx > 0 else -1
    for y_idx in range(min([y0, yn]), max([y0, yn]) + ystep, ystep):
        for x_idx in range(min([x0, xn]), max([x0, xn]) + xstep, xstep):
            if command == 'on':
                lights[y_idx][x_idx] += 1
            elif command == 'off':
                lights[y_idx][x_idx] -= 1
                if lights[y_idx][x_idx] < 0:
                    lights[y_idx][x_idx] = 0
            elif command == 'toggle':
                lights[y_idx][x_idx] += 2
            else:
                print(f"Unknown command {command}")


def total_brightness():
    intensity = 0
    for y in lights:
        intensity += sum(y)
    return intensity


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    init_lights()
    # print(f"Number on = {number_on()}")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()

            spaces = tmp.count(' ')
            words = tmp.split()
            command, topleft, bottomright = None, None, None
            if spaces == 3:
                # toggle
                command, topleft, bottomright = words[0], words[1], words[3]
                # print(f"{command}, {topleft}, {bottomright}")
            elif spaces == 4:
                # turn on/off
                command, topleft, bottomright = words[1], words[2], words[4]
                # print(f"{command}, {topleft}, {bottomright}")

            tmp = topleft.split(',')
            x_0, y_0 = int(tmp[0]), int(tmp[1])
            tmp = bottomright.split(',')
            x_n, y_n = int(tmp[0]), int(tmp[1])
            # print(f"{command} from ({x_0},{y_0}) to ({x_n},{y_n})")

            handle_command(command, x_0, y_0, x_n, y_n)
        print(f"Total brightness = {total_brightness()}")


if __name__ == '__main__':
    main()
