def f(x, stop, step):
    if x > stop:
        return 0
    if x == stop:
        return 1

    return f(x + 1, stop, step + 1) + f(x + 2, stop, step + 1)


print(f(1, 3, 0))
