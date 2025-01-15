from rtz import rtz


def p_non_assoc(m):

    tot_events = 0
    non_assoc_events = 0

    for h in range(2, m):

        for k in range(1, h):

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

    prob = non_assoc_events / tot_events
    return prob


print("\n" * 64)
m_val = int(input("m = "))

p = p_non_assoc(m_val)
print("\nP(non-associativity) = " + str(p))
