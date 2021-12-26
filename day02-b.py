import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    total_area, total_length = 0, 0
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            l_str, w_str, h_str = tmp.split('x')
            l, w, h = int(l_str), int(w_str), int(h_str)
            base_area = 2*l*w + 2*w*h + 2*h*l
            slack_area = min([l*w, w*h, h*l])
            box_area = base_area + slack_area
            print(f"Area for this box = {box_area}")

            sides = [l, w, h]
            sides.sort()
            short_a, short_b = sides[0], sides[1]
            ribbon_length = 2 * short_a + 2 * short_b
            bow_length = l * w * h
            box_length = ribbon_length + bow_length
            print(f"Length for this box = {box_length}")

            total_area += box_area
            total_length += box_length
    print(f"Total area to order = {total_area}")
    print(f"Total length to order = {total_length}")


if __name__ == '__main__':
    main()
