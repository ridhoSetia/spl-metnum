def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print(["{0:8.4f}".format(x) for x in row])

def gauss_jordan(a, b):
    n = len(a)
    aug = [a[i] + [b[i]] for i in range(n)]

    print_matrix(aug, "Augmented Matrix Awal")

    for i in range(n):
        print(f"\nLangkah {i+1}:")
        pivot = aug[i][i]
        print(f"Pivot pada baris {i+1}: {pivot:.4f}")

        # Skala pivot ke 1
        print(f"Normalisasi baris {i+1} dengan membagi seluruh elemen dengan {pivot:.4f}")
        for j in range(i, n+1):
            aug[i][j] /= pivot

        print_matrix(aug, f"Setelah normalisasi baris {i+1}")

        # Nol-kan elemen lain di kolom
        for k in range(n):
            if k != i:
                ratio = aug[k][i]
                print(f"Eliminasi elemen di baris {k+1}, kolom {i+1} dengan rasio {ratio:.4f}")
                for j in range(i, n+1):
                    before = aug[k][j]
                    aug[k][j] -= ratio * aug[i][j]
                    print(f"  aug[{k+1}][{j+1}] = {before:.4f} - ({ratio:.4f} * {aug[i][j]:.4f}) = {aug[k][j]:.4f}")
        print_matrix(aug, f"Matrix setelah langkah Gauss-Jordan ke-{i+1}")

    x = [aug[i][-1] for i in range(n)]
    print("\nHasil solusi (Gauss Jordan):", x)
    return x
