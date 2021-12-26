import sys


def calc_score(cook, quants):
    sum_c, sum_d, sum_f, sum_t, sum_kcal = 0, 0, 0, 0, 0
    for idx in range(len(cook)):
        (name, c, d, f, t, kcal) = cook[idx]
        # print(f"{name}: {c} {d} {f} {t} {kcal}")
        sum_c += quants[idx]*c
        sum_d += quants[idx]*d
        sum_f += quants[idx]*f
        sum_t += quants[idx]*t
        sum_kcal += quants[idx]*kcal
    score = (0 if sum_c < 0 else sum_c)
    score *= (0 if sum_d < 0 else sum_d)
    score *= (0 if sum_f < 0 else sum_f)
    score *= (0 if sum_t < 0 else sum_t)
    score = (0 if sum_kcal != 500 else score)
    # print(f"{quants} -> {score}")
    return score


def main():
    if len(sys.argv) != 2:
        sys.exit("Please provide a file name for input data")

    cookies = []
    filename = sys.argv[1]
    with open(filename, "r") as inputfile:
        while True:
            line = inputfile.readline()
            if not line:
                break
            tmp = line.strip()
            # print(f"{tmp}")

            name, attributes = tmp.split(':')
            cap, dur, fla, tex, cal = attributes.split(',')
            capacity = int(cap.split()[1])
            durability = int(dur.split()[1])
            flavor = int(fla.split()[1])
            texture = int(tex.split()[1])
            calories = int(cal.split()[1])
            print(f"{name}: Capacity = {capacity} Durability = {durability} Flavor = {flavor} Texture = {texture} Calories = {calories}")
            tt = (name, capacity, durability, flavor, texture, calories)
            cookies.append(tt)

    best_score = None
    best_recipe = None
    for a in range(101):
        for b in range(101):
            if a+b <= 100:
                for c in range(101):
                    if a+b+c <= 100:
                        d = 100 - (a+b+c)
                        if d >= 0:
                            ratio = [a, b, c, d]
                            # print(f"  {ratio} = {sum(ratio)}")
                            score = calc_score(cookies, ratio)
                            if best_score is None or score > best_score:
                                best_score = score
                                best_recipe = ratio

    print(f"Best 500 calories score is {best_score} with recipe {best_recipe}")


if __name__ == '__main__':
    main()