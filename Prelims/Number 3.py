"""
Numerical Analysis Prelim Exam - Problem 3
Fixed-Point Iteration: x^3 + x - 4 = 0,  x0 = 1.5,  accurate to 3 decimal places.

"Fastest convergence" = choose the rearrangement x = g(x) whose |g'(r)| is
smallest near the root. Three candidate rearrangements are compared below.
"""

import math


def f(x):
    return x ** 3 + x - 4


# ---- candidate rearrangements of x^3 + x - 4 = 0 into x = g(x) --------------

CANDIDATES = {
    "g1(x) = (4 - x)^(1/3)": (
        lambda x: (4 - x) ** (1 / 3),
        lambda x: -1 / 3 * (4 - x) ** (-2 / 3),
    ),
    "g2(x) = 4 / (x^2 + 1)": (
        lambda x: 4 / (x * x + 1),
        lambda x: -8 * x / (x * x + 1) ** 2,
    ),
    "g3(x) = 4 - x^3": (
        lambda x: 4 - x ** 3,
        lambda x: -3 * x * x,
    ),
}


def compare_candidates(r):
    print("Convergence test:  |g'(r)| < 1 is required; smaller is faster.\n")
    print(f"{'rearrangement':<24} {'g\'(r)':>10} {'|g\'(r)|':>10}   verdict")
    print("-" * 62)
    for name, (g, gp) in CANDIDATES.items():
        d = gp(r)
        verdict = "converges" if abs(d) < 1 else "DIVERGES"
        print(f"{name:<24} {d:>10.5f} {abs(d):>10.5f}   {verdict}")
    print()


def fixed_point(g, x0, tol=5e-5, max_iter=50):
    print(f"{'n':>2} {'x_n':>12} {'g(x_n)':>12} {'|x_n+1 - x_n|':>15}")
    print("-" * 45)

    x = x0
    for n in range(max_iter):
        x_new = g(x)
        print(f"{n:>2} {x:>12.6f} {x_new:>12.6f} {abs(x_new - x):>15.6f}")
        if abs(x_new - x) < tol:
            return x_new, n + 1
        x = x_new

    raise RuntimeError("Did not converge within max_iter.")


if __name__ == "__main__":
    print("Problem 3:  x^3 + x - 4 = 0,  x0 = 1.5,  3 decimal places\n")

    compare_candidates(1.378797)  # approximate root, used only for the test

    print("Fastest convergence -> use g(x) = (4 - x)^(1/3)\n")
    g = CANDIDATES["g1(x) = (4 - x)^(1/3)"][0]
    root, steps = fixed_point(g, 1.5)

    print("-" * 45)
    print(f"Iterations     : {steps}")
    print(f"Root (3 d.p.)  : {root:.3f}")
    print(f"Root (6 d.p.)  : {root:.6f}")
    print(f"f(root)        : {f(root):.6e}")