"""
This module handles user authentication and authorization.
It includes functions for login, logout, and permission checks.
"""


def max_weight(v, s, n):
    """
    This module handles user authentication and authorization.
    It includes functions for login, logout, and permission checks.
    """
    print(n)

    if n < 0:
        return 0
    if s[n] == -1:
        s[n] = max(max_weight(v, s, n - 1), (max_weight(v, s, n - 2) + v[n]))
    return s[n]


def max_weight_wrapper(v, s, n):
    """
    fuck you
    """
    return max_weight(v, s, n - 1)


def max_iterative(v, n):
    """
    aids
    """
    if n == 0:
        return v[0]
    if n == 1:
        return max(v[0], v[1])
    w1 = v[0]
    w2 = max(v[0], v[1])

    for i in range(2, n + 1):
        w3 = max(w2, v[i] + w1)
        w1 = w2
        w2 = w3
    return w2


def explain(v, s, n):
    res = []
    i = n
    while i >= 2:
        if s[i] == s[i - 2] + v[i]:
            res.append(v[i])
            i = i - 1

        i = i - 1

    print(i)
    if i == 0:
        res.append(v[0])

    res2 = res[::-1]
    return res2


def main():
    """
    shut up
    """
    v = [100, 54, 4432, 543, 5, 455, 546, 2436, 54]
    s = [-1] * len(v)
    print("max is", max_weight_wrapper(v, s, len(v) - 1))
    res = explain(v, s, len(v) - 1)
    print("used", res)
    tot = 0

    for val in res:
        tot += val
    print("total", tot)


if __name__ == "__main__":
    # code to execute when script is run directly
    main()
