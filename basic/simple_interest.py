p, r, t = [
    float(x)
    for x in input(
        "Enter the principal amount, rate and time separated by spaces: "
    ).split()
]

print(f"interest: {p*r*t/100}")  # noqa
