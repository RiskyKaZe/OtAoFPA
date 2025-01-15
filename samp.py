import random
from rtz import rtz
import time


def samp(m, act_prob):

    tot_events = 0
    non_assoc_events = 0
    prob = 0
    perc_diff = 1

    while perc_diff >= 0.025 or perc_diff <= -0.025:

        for h in range(2, m):

            for k in range(1, m - 1):

                c_int = random.randint(2 ** m, 2 ** (m + 1) - 1)
                b_float = random.randint(2 ** m, 2 ** (m + 1) - 1) / (2 ** k)
                a_float = random.randint(2 ** m, 2 ** (m + 1) - 1) / (2 ** h)

                ineq_left = rtz(rtz(c_int + b_float, m) - a_float, m)
                ineq_right = rtz(c_int + rtz(b_float - a_float, m), m)

                if ineq_left != ineq_right:
                    tot_events = tot_events + 1
                    non_assoc_events = non_assoc_events + 1

                else:
                    tot_events = tot_events + 1

        prob = non_assoc_events / tot_events
        perc_diff = (prob - act_prob) / act_prob

    print("\nTotal Events = " + str(tot_events))
    print("Non-Associativity Events = " + str(non_assoc_events))

    return prob


print("\n" * 64)
m_val = int(input("m = "))
p_val = float(input("P = "))

time_start = time.time()
p = samp(m_val, p_val)
time_end = time.time()
time_taken = time_end - time_start

print("\nP(non-associativity) = " + str(p))
print("Runtime = " + str(time_taken))
