def hcf_v1(n1: int, n2: int) -> int:
    i = 2
    hcf = 1
    if n1 > n2:
        n1, n2 = n2, n1
    while i <= n1:  # less than smaller number
        if n1 % i == 0 and n2 % i == 0:
            n1 //= i
            n2 //= i
            hcf *= i
        else:
            i += 1
    return hcf


def hcf_v2(n1: int, n2: int) -> int:
    if n2 > n1:
        n1, n2 = n2, n1
    return n1 if n2 == 0 else hcf_v2(n1 % n2, n2)


if __name__ == "__main__":
    print(f"{hcf_v1(2400000, 239000080)}")
    print(f"{hcf_v2(2400000, 239000080)}")
