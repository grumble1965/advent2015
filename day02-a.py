import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    total_area = 0
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
            total_area += box_area
    print(f"Total area to order = {total_area}")

if __name__ == '__main__':
    main()
