def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print(["{0:8.4f}".format(x) for x in row])
        
def gauss_seidel(a, b, tol=1e-6, max_iter=100):
    n = len(a)
    x = [0.0] * n
    for itr in range(max_iter):
        x_new = x.copy()
        print(f"\nIterasi Gauss-Seidel ke-{itr+1}:")
        for i in range(n):
            s1 = sum(a[i][j] * x_new[j] for j in range(i))
            s2 = sum(a[i][j] * x[j] for j in range(i + 1, n))
            
            # Rincian perhitungan
            s1_detail = ' + '.join([f"{a[i][j]:.4f}*{x_new[j]:.4f}" for j in range(i)]) or "0"
            s2_detail = ' + '.join([f"{a[i][j]:.4f}*{x[j]:.4f}" for j in range(i + 1, n)]) or "0"

            numerator = b[i] - s1 - s2
            denominator = a[i][i]
            result = numerator / denominator

            print(f"x[{i}] = ({b[i]:.4f} - ({s1_detail}) - ({s2_detail})) / {a[i][i]:.4f} = {result:.6f}")
            x_new[i] = result

        print("x =", [f"{val:.6f}" for val in x_new])
        print([abs(x_new[i] - x[i]) < tol for i in range(n)])
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            print("\nKonvergen. Iterasi dihentikan.")
            break
        x = x_new
    print("\nHasil solusi (Gauss-Seidel):", [f"{val:.6f}" for val in x])
    return x
