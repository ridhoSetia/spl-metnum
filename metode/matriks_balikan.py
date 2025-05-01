def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print(["{0:8.4f}".format(x) for x in row])

def inverse_matrix(a):
    n = len(a)
    identity = [[float(i == j) for j in range(n)] for i in range(n)]
    aug = [a[i] + identity[i] for i in range(n)]

    print_matrix(aug, "Augmented Matrix (untuk invers)")

    # Gauss-Jordan untuk invers
    for i in range(n):
        pivot = aug[i][i]
        print(f"\nLangkah {i+1}: Membuat pivot ke-{i+1} menjadi 1 dengan membagi baris {i+1} dengan {pivot:.4f}")
        for j in range(2*n):
            aug[i][j] /= pivot

        print_matrix(aug, f"Setelah skala pivot baris {i+1}")

        for k in range(n):
            if k != i:
                ratio = aug[k][i]
                print(f" - Eliminasi elemen di baris {k+1}, kolom {i+1} dengan mengurangkan {ratio:.4f} * baris {i+1}")
                for j in range(2*n):
                    aug[k][j] -= ratio * aug[i][j]

        print_matrix(aug, f"Matrix setelah langkah invers ke-{i+1}")

    inv = [row[n:] for row in aug]
    return inv

def inverse_solve(a, b):
    print("\n=== Mencari Invers Matriks A ===")
    inv = inverse_matrix(a)
    print_matrix(inv, "Invers A")

    print("\n=== Mengalikan Invers A dengan B untuk Mendapatkan Solusi ===")
    x = []
    for i in range(len(a)):
        total = 0
        terms = []
        for j in range(len(b)):
            term = inv[i][j] * b[j]
            terms.append(f"{inv[i][j]:.4f} * {b[j]:.4f}")
            total += term
        print(f"x[{i+1}] = {' + '.join(terms)} = {total:.4f}")
        x.append(total)

    print("\nHasil solusi (Matriks Balikan):", x)
    return x
