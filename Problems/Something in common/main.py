def common_part(y):
    print("Value of the function equals", y)


def calculate_linear(k, b, x):
    y = k * x + b
    common_part(y)
    return y


def calculate_quadratic(a, b, c, x):
    y = (a * x * x) + (b * x) + c
    common_part(y)
    return y


# create function common_part
