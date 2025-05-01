def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print(["{0:8.4f}".format(x) for x in row])
        
def jacobi(a, b, tol=1e-6, max_iter=100):
    n = len(a)
    x = [0.0]*n
    for itr in range(max_iter):
        x_new = x.copy()
        print(f"\nIterasi Jacobi ke-{itr+1}:")
        for i in range(n):
            s_terms = [f"{a[i][j]:.4f}*{x[j]:.4f}" for j in range(n) if j != i]
            s = sum(a[i][j]*x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / a[i][i]
            print(
                f"x[{i}] = ({b[i]:.4f} - ({' + '.join(s_terms)})) / {a[i][i]:.4f} = {x_new[i]:.6f}"
            )
        print("x =", ["{:.6f}".format(val) for val in x_new])
        print([abs(x_new[i] - x[i]) < tol for i in range(n)])
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            print("\nKonvergen. Iterasi dihentikan.")
            break
        x = x_new
    print("\nHasil solusi (Jacobi):", x)
    return x
