import sys
import itertools

input_str = ''
output_str = ''


def main():
    global input_str
    global output_str

    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()

            # iter = 0
            # for ll in look_and_say(tmp, 50):
            #     print(f"Iteration {iter}  Length {len(ll)}")
            #     iter += 1

            for i in range(50):
                input_str = tmp
                iteration()
                print(f"{i+1}: {len(output_str)}")
                tmp = output_str


def iteration():
    global input_str
    global output_str
    last_character, counter = None, 0
    output_list = []
    for ch in input_str:
        if last_character is not None and ch == last_character:
            counter += 1
        elif last_character is None:
            last_character = ch
            counter = 1
        elif last_character != ch:
            output_list.append(str(counter))
            output_list.append(last_character)
            # output_str = output_str + str(counter) + last_character
            last_character = ch
            counter = 1
        else:
            print("What?")
    output_list.append(str(counter))
    output_list.append(last_character)
    # output_str = output_str + str(counter) + last_character
    output_str = "".join(output_list)
    return


def look_and_say(generator, length):
    value = generator
    yield value
    for i in range(length):
        value = sum(([len(list(g)), k] for k, g in itertools.groupby(value)), [])
        yield value


if __name__ == '__main__':
    main()
