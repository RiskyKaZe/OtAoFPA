import random
import math
total_non_assoc = 0
num_trials = 10000
m = int(input("m: "))

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
def sampling(m):
    global total_prob
    for h in range(2, m):  # h starts from 2 and goes to m-1
        print("h:", h)
        for k in range(1, h):  # k ranges from 1 to h-1
            print("  k:", k)
            c = random.randint(2**m,2**(m+1)-1)
            print(c)
            b_val = random.randint(2**m,2**(m+1)-1)
            b = b_val/(2**k)
            print(b)
            a_val = random.randint(2**m,2**(m+1)-1)
            a = a_val/(2**h)
            print(a)
            eq_left = rtz((rtz((c+b),m)-a),m)
            eq_right = rtz((rtz((b-a),m)+c),m)
            if eq_left != eq_right:
                return 1
    return 0
    return non_assoc
for _ in range(num_trials):
    non_assoc = sampling(m)
    total_non_assoc += non_assoc
print(f"The probability is {total_non_assoc/num_trials:.10g}")

