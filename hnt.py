def hnt(n, A, B, C):
    if n == 1:
        print(A, "=>", C)
    if n > 1:
        hnt(n - 1, A, C, B)
        hnt(1, A, B, C)
        hnt(n - 1, B, A, C)


hnt(4, "A", "B", "C")
