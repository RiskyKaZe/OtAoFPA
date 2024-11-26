import math
import time


def rtz(num, m):

    if num > 0:
        rounded_num = math.floor(num)
        if rounded_num >= (2 ** (m + 1)):
            rounded_num = rounded_num - (rounded_num % 2)

    elif num < 0:
        rounded_num = math.ceil(num)
        if rounded_num <= (2 ** (m + 1)):
            rounded_num = rounded_num + (rounded_num % 2)

    else:
        rounded_num = 0

    return rounded_num


def p_non_assoc(m):

    tot_events = 0
    non_assoc_events = 0

    for h_val in range(2, m):

        h = h_val

        for k_val in range(1, m - 1):

            k = k_val

            for c_int in range(2 ** m, 2 ** (m + 1)):

                for b_int in range(2 ** m, 2 ** (m + 1)):

                    b_float = b_int / (2 ** k)

                    for a_int in range(2 ** m, 2 ** (m + 1)):

                        a_float = a_int / (2 ** h)

                        ineq_left = rtz(rtz(c_int + b_float, m) - a_float, m)
                        ineq_right = rtz(c_int + rtz(b_float - a_float, m), m)

                        if ineq_left != ineq_right:
                            tot_events = tot_events + 1
                            non_assoc_events = non_assoc_events + 1

                        else:
                            tot_events = tot_events + 1

    print("\nTotal Events = " + str(tot_events))
    print("Non-Associativity Events = " + str(non_assoc_events))

    probability = non_assoc_events / tot_events
    return probability


print("\n" * 64)
m_val = int(input("m = "))

time_start = time.time()
p = p_non_assoc(m_val)
time_end = time.time()
time_taken = time_end - time_start

print("\nP(non-associativity) = " + str(p))
print("Runtime = " + str(time_taken))
