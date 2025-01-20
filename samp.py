import random
from rtz import rtz
import time


def samp(m, act_prob):

    tot_events = 0
    non_assoc_events = 0
    prob = 0
    perc_diff = 1
    samples = 0

#    tot_cases = (2 ** (3 * m)) * (((m - 2)(m - 1)) / 2)

    while perc_diff >= 0.025 or perc_diff <= -0.025:

        samples = samples + 1
        c_int = []
        b_float = []
        a_float = []

        for h in range(2, m):

            for k in range(1, h):

                for s in range(samples + 1):

                    c_int.append(random.randint(2 ** m, 2 ** (m + 1) - 1))
                    b_float.append(random.randint(2 ** m, 2 ** (m + 1) - 1) / (2 ** k))
                    a_float.append(random.randint(2 ** m, 2 ** (m + 1) - 1) / (2 ** h))

                for ss in range(samples + 1):

                    ineq_left = rtz(rtz(c_int[ss] + b_float[ss], m) - a_float[ss], m)
                    ineq_right = rtz(c_int[ss] + rtz(b_float[ss] - a_float[ss], m), m)

                    if ineq_left != ineq_right:

                        tot_events = tot_events + 1
                        non_assoc_events = non_assoc_events + 1

                    else:

                        tot_events = tot_events + 1

        prob = non_assoc_events / tot_events
        perc_diff = (prob - act_prob) / act_prob

    print("\nSamples = " + str(samples))
    print("Total Events = " + str(tot_events))
    print("Non-Associativity Events = " + str(non_assoc_events))
    print("Percentage Difference: " + str(perc_diff) + "%")

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
