"""
Numerical Analysis Prelim Exam - Problem 1
Bisection Method: f(x) = cos(x) - x  on the interval [0, 1], 6 iterations.
"""

import math


def f(x):
    return math.cos(x) - x


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
    print("Problem 1:  f(x) = cos(x) - x   on [0, 1]   for 6 iterations\n")

    a, b = bisection(f, 0.0, 1.0, 6)
    root = (a + b) / 2

    print("-" * 74)
    print(f"Final interval : [{a:.6f}, {b:.6f}]")
    print(f"Root (midpoint): {root:.6f}")
    print(f"f(root)        : {f(root):.6e}")
    print(f"Max error      : {(b - a) / 2:.6f}")
    print(f"True root      : 0.739085")