import math
import random

num_trials = 100
non_assoc_count = 0
total_non_assoc = 0

m = int(input("m: "))
e = int((m-1)*(m-2)/2)
v = (num_trials)*(num_trials+1)/2
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
def sampling(m, num_trials):
    global non_assoc_count
    for h in range(2, m):  # h starts from 2 and goes to m-1
        print("h:", h)
        for k in range(1, h):
            print("  k:", k)
            for _ in range(num_trials):
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
                    non_assoc_count += 1
    return non_assoc_count
for _ in range(num_trials):
    non_assoc = sampling(m, num_trials)
    total_non_assoc += non_assoc_count
ee = int(e * num_trials * v)
print(f"Total events is: {ee}")
probability = total_non_assoc/ee
print("e:", e)
print(f"The probability is {probability:.10g}")
