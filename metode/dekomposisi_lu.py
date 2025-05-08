def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print(["{0:8.4f}".format(x) for x in row])

def lu_decomposition(a, b):
    n = len(a)
    L = [[0.0]*n for _ in range(n)]
    U = [[0.0]*n for _ in range(n)]

    print("\nLangkah 1: Decomposisi Matriks A menjadi L dan U")
    for i in range(n):
        print(f"\nIterasi ke-{i+1}:")

        # Hitung elemen-elemen matriks U
        for j in range(i, n):
            total = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = a[i][j] - total
            detail = ' + '.join([f"{L[i][k]:.4f}*{U[k][j]:.4f}" for k in range(i)]) or "0"
            print(f"U[{i}][{j}] = {a[i][j]:.4f} - ({detail}) = {U[i][j]:.6f}")

        # Hitung elemen-elemen matriks L
        for j in range(i, n):
            if i == j:
                L[j][i] = 1.0  # diagonal L selalu 1
                print(f"L[{j}][{i}] di-set menjadi 1 (diagonal utama)")
            else:
                total = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (a[j][i] - total) / U[i][i]
                detail = ' + '.join([f"{L[j][k]:.4f}*{U[k][i]:.4f}" for k in range(i)]) or "0"
                print(f"L[{j}][{i}] = ({a[j][i]:.4f} - ({detail})) / {U[i][i]:.4f} = {L[j][i]:.6f}")

    print_matrix(L, "Matrix L")
    print_matrix(U, "Matrix U")

    # Substitusi maju: Ly = b
    print("\nLangkah 2: Substitusi Maju untuk menyelesaikan Ly = b")
    y = [0.0]*n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j]*y[j] for j in range(i))
        print(f"y[{i}] = {b[i]} - " +
              " - ".join([f"L[{i}][{j}]*y[{j}]" for j in range(i)]) +
              f" = {y[i]:.4f}")

    # Substitusi balik: Ux = y
    print("\nLangkah 3: Substitusi Balik untuk menyelesaikan Ux = y")
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))) / U[i][i]
        print(f"x[{i}] = ({y[i]} - " +
              " - ".join([f"U[{i}][{j}]*x[{j}]" for j in range(i+1, n)]) +
              f") / {U[i][i]:.4f} = {x[i]:.4f}")

    print("\nHasil solusi (Dekomposisi Lu):", x)
    return x