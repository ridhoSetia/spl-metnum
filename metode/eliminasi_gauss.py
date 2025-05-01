def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print(["{0:8.4f}".format(x) for x in row])

def gauss_elimination(a, b):
    n = len(a)
    aug = [a[i] + [b[i]] for i in range(n)]

    print_matrix(aug, "Augmented Matrix Awal")

    # Eliminasi Maju
    for i in range(n):
        print(f"\n=== Langkah Eliminasi untuk baris {i+1} ===")

        # Pivoting (jika diperlukan)
        max_row = max(range(i, n), key=lambda r: abs(aug[r][i]))
        if i != max_row:
            aug[i], aug[max_row] = aug[max_row], aug[i]
            print(f"Tukar baris {i+1} dengan baris {max_row+1} (pivoting)")
            print_matrix(aug, "Setelah Pertukaran Baris")

        pivot = aug[i][i]
        print(f"Pivot: aug[{i}][{i}] = {pivot:.4f}")

        for j in range(i+1, n):
            ratio = aug[j][i] / pivot
            print(f"\nMengeliminasi baris {j+1} dengan rasio = aug[{j}][{i}] / aug[{i}][{i}] = {aug[j][i]:.4f} / {pivot:.4f} = {ratio:.4f}")
            for k in range(i, n+1):
                old_val = aug[j][k]
                aug[j][k] -= ratio * aug[i][k]
                print(f"aug[{j}][{k}] = {old_val:.4f} - ({ratio:.4f} * {aug[i][k]:.4f}) = {aug[j][k]:.4f}")
        print_matrix(aug, f"Matrix setelah eliminasi baris {i+1}")

    # Substitusi Balik
    x = [0 for _ in range(n)]
    print("\n=== Substitusi Balik ===")
    for i in range(n-1, -1, -1):
        total = sum(aug[i][j]*x[j] for j in range(i+1, n))
        numerator = aug[i][n] - total
        x[i] = numerator / aug[i][i]
        print(
            f"x[{i}] = ({aug[i][n]:.4f} - "
            f"{' + '.join([f'{aug[i][j]:.4f}*{x[j]:.4f}' for j in range(i+1, n)]) if i < n-1 else '0'}) "
            f"/ {aug[i][i]:.4f} = {x[i]:.4f}"
        )

    print("\nHasil solusi (Eliminasi Gauss):", x)
    return x
