import math
import matplotlib.pyplot as plt

# 1.1 Computer Problems -- Bisection Method
# just implementing bisection once and reusing it for every part


def bisection(f, a, b, decimals=6, max_iter=200):
    """
    Standard bisection method.

    f        : function, f(x) = 0 is what we're solving
    a, b     : endpoints of an interval where f changes sign
    decimals : how many correct decimal places we want
    max_iter : safety cap on iterations

    Returns the approximate root, iteration count, and the
    iteration history (for printing a table).
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError(f"f(a) and f(b) have the same sign on [{a}, {b}] -- no guaranteed root here")

    tol = 0.5 * 10 ** (-decimals)
    history = []

    for n in range(1, max_iter + 1):
        mid = (a + b) / 2
        fmid = f(mid)
        history.append((n, a, b, mid, fmid))

        if abs(fmid) == 0 or (b - a) / 2 < tol:
            return mid, n, history

        if fa * fmid < 0:
            b, fb = mid, fmid
        else:
            a, fa = mid, fmid

    print("WARNING: max iterations reached without full convergence")
    return (a + b) / 2, max_iter, history


def show_table(title, root, decimals, iters, history):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)
    print(f"root ~ {root:.{decimals}f}   ({iters} iterations)")
    print(f"{'n':>4} {'a':>15} {'b':>15} {'mid':>15} {'f(mid)':>15}")
    print("-" * 70)
    for n, a, b, mid, fmid in history:
        print(f"{n:>4} {a:>15.8f} {b:>15.8f} {mid:>15.8f} {fmid:>15.2e}")


# ==========================================================
# PROBLEM 1 -- bisection to 6 correct decimal places
# ==========================================================
print("\n" + "#" * 70)
print("PROBLEM 1 -- six decimal places")
print("#" * 70)

# 1a: x^3 = 9  ->  f(x) = x^3 - 9
# quick check: f(2) = -1, f(3) = 18, so root is bracketed by [2, 3]
f1a = lambda x: x**3 - 9
root, n, hist = bisection(f1a, 2, 3, decimals=6)
show_table("1(a): x^3 = 9", root, 6, n, hist)

# 1b: 3x^3 + x^2 = x + 5  ->  f(x) = 3x^3 + x^2 - x - 5
# f(1) = -2, f(1.5) ~ 5.9, root somewhere in [1, 1.5]
f1b = lambda x: 3 * x**3 + x**2 - x - 5
root, n, hist = bisection(f1b, 1, 1.5, decimals=6)
show_table("1(b): 3x^3 + x^2 = x + 5", root, 6, n, hist)

# 1c: cos^2(x) + 6 = x  ->  f(x) = cos(x)^2 + 6 - x
# f(6) ~ 0.92, f(7) ~ -0.43, root in [6, 7]
f1c = lambda x: math.cos(x) ** 2 + 6 - x
root, n, hist = bisection(f1c, 6, 7, decimals=6)
show_table("1(c): cos^2(x) + 6 = x", root, 6, n, hist)


# ==========================================================
# PROBLEM 2 -- bisection to 8 correct decimal places
# ==========================================================
print("\n" + "#" * 70)
print("PROBLEM 2 -- eight decimal places")
print("#" * 70)

# 2a: x^5 + x = 1  ->  f(x) = x^5 + x - 1
# f(0) = -1, f(1) = 1, root in [0, 1]
f2a = lambda x: x**5 + x - 1
root, n, hist = bisection(f2a, 0, 1, decimals=8)
show_table("2(a): x^5 + x = 1", root, 8, n, hist)

# 2b: sin(x) = 6x + 5  ->  f(x) = sin(x) - 6x - 5
# f(-1) ~ 0.16, f(-0.9) ~ -0.38, root in [-1, -0.9]
f2b = lambda x: math.sin(x) - 6 * x - 5
root, n, hist = bisection(f2b, -1, -0.9, decimals=8)
show_table("2(b): sin(x) = 6x + 5", root, 8, n, hist)

# 2c: ln(x) + x^2 = 3  ->  f(x) = ln(x) + x^2 - 3
# f(1.5) ~ -0.34, f(1.6) ~ 0.03, root in [1.5, 1.6]
f2c = lambda x: math.log(x) + x**2 - 3
root, n, hist = bisection(f2c, 1.5, 1.6, decimals=8)
show_table("2(c): ln(x) + x^2 = 3", root, 8, n, hist)


# ==========================================================
# PROBLEM 3 -- locate ALL solutions, sketch, pick 3 unit
# intervals that each bracket a root, then solve to 6 places
# ==========================================================
print("\n" + "#" * 70)
print("PROBLEM 3 -- locating all roots")
print("#" * 70)

# equations rewritten as f(x) = 0
f3a = lambda x: 2 * x**3 - 6 * x - 1
f3b = lambda x: math.exp(x - 2) + x**3 - x
f3c = lambda x: 1 + 5 * x - 6 * x**3 - math.exp(2 * x)


def sketch(f, xmin, xmax, title, filename, intervals=None):
    """Plot f over [xmin, xmax] and mark the bracketing intervals we picked."""
    xs = [xmin + i * (xmax - xmin) / 800 for i in range(801)]
    ys = [f(x) for x in xs]

    plt.figure(figsize=(7, 4.5))
    plt.axhline(0, color="black", linewidth=0.8)
    plt.plot(xs, ys, color="steelblue")

    if intervals:
        for a, b in intervals:
            plt.axvspan(a, b, color="orange", alpha=0.2)

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=130)
    plt.close()


# 3a: plotting shows sign changes at roughly [-2,-1], [-1,0], [1,2]
brackets_3a = [(-2, -1), (-1, 0), (1, 2)]
sketch(f3a, -3, 3, "3(a): 2x^3 - 6x - 1", "/home/jlry-dev/School/Elec2/plot_3a.png", brackets_3a)

print("\n3(a): 2x^3 - 6x - 1 = 0 -- three roots, one in each shaded interval")
for a, b in brackets_3a:
    root, n, hist = bisection(f3a, a, b, decimals=6)
    print(f"  interval [{a}, {b}] -> root ~ {root:.6f}  ({n} iterations)")

# 3b: the two roots near 0 end up close together, so instead of the
# usual integer intervals we use [-1.5,-0.5], [-0.5,0.5], [0.5,1.5],
# which is what the plot suggests once you zoom in near the origin
brackets_3b = [(-1.5, -0.5), (-0.5, 0.5), (0.5, 1.5)]
sketch(f3b, -3, 3, "3(b): e^(x-2) + x^3 - x", "/home/jlry-dev/School/Elec2/plot_3b.png", brackets_3b)

print("\n3(b): e^(x-2) + x^3 - x = 0")
for a, b in brackets_3b:
    root, n, hist = bisection(f3b, a, b, decimals=6)
    print(f"  interval [{a}, {b}] -> root ~ {root:.6f}  ({n} iterations)")

# 3c: same situation as 3b -- two roots sit close to each other near x=0
brackets_3c = [(-1.5, -0.5), (-0.5, 0.5), (0.5, 1.5)]
sketch(f3c, -3, 3, "3(c): 1 + 5x - 6x^3 - e^(2x)", "/home/jlry-dev/School/Elec2/plot_3c.png", brackets_3c)

print("\n3(c): 1 + 5x - 6x^3 - e^(2x) = 0")
for a, b in brackets_3c:
    root, n, hist = bisection(f3c, a, b, decimals=6)
    print(f"  interval [{a}, {b}] -> root ~ {root:.6f}  ({n} iterations)")


print("\n" + "#" * 70)
print("done")
print("#" * 70)
