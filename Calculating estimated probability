total_prob = 0
m = int(input("m: "))
def all_combinations(m):
    global total_prob
    for h in range(2, m):  # h starts from 2 and goes to m-1
        print("h:", h)
        for k in range(1, h):  # k ranges from 1 to h-1
            print("  k:", k)
            W = 1 - 3 * (2 ** (-k - 1)) + 2 ** (-m - 1)
            X = 0.5 + 2 ** (-k - 1) - 2 ** (-h)
            Y = 1 - 3 * (2 ** (-k - 1)) + 3 * (2 ** (-h - 1)) - 2 ** (-m - h) + 2 ** (-m)
            Z = 1 - 2 ** (-h)
            P_non_associative = (
                    - (W * X * Y * Z) / 2
                    - (W * X * Y) / 4
                    + (W * X * Z) / 2
                    + (W * X) / 2
                    + (W * Y) / 4
                    - W
                    - (X * Y * Z) / 2
                    + (X * Y) / 4
                    + (X * Z) / 2
                    - X / 2
                    - Y / 4
                    + 1
            )
            total_prob += P_non_associative
    print(total_prob)
all_combinations(m)
