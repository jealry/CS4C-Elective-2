"""
Numerical Analysis Prelim Exam - Problem 2
Bisection Method: f(x) = tan(x) - 2  on the interval [1.0, 1.5], 6 iterations.

Note: x is in RADIANS. The true root is arctan(2) = 1.107149.
"""

import math


def f(x):
    return math.tan(x) - 2


def bisection(f, a, b, iterations):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    print(f"{'i':>2} {'a':>10} {'b':>10} {'c':>10} {'f(a)':>12} {'f(c)':>12}  Decision")
    print("-" * 74)

    for i in range(1, iterations + 1):
        c = (a + b) / 2
        fa, fc = f(a), f(c)

        if fa * fc < 0:
            decision = "f(a)f(c) < 0  ->  b = c"
        else:
            decision = "f(a)f(c) > 0  ->  a = c"

        print(f"{i:>2} {a:>10.6f} {b:>10.6f} {c:>10.6f} {fa:>12.6f} {fc:>12.6f}  {decision}")

        if fa * fc < 0:
            b = c
        else:
            a = c

    return a, b


if __name__ == "__main__":
    print("Problem 2:  f(x) = tan(x) - 2   on [1.0, 1.5]   for 6 iterations\n")

    a, b = bisection(f, 1.0, 1.5, 6)
    root = (a + b) / 2

    print("-" * 74)
    print(f"Final interval : [{a:.6f}, {b:.6f}]")
    print(f"Root (midpoint): {root:.6f}")
    print(f"f(root)        : {f(root):.6e}")
    print(f"Max error      : {(b - a) / 2:.6f}")
    print(f"True root      : {math.atan(2):.6f}  (= arctan 2)")