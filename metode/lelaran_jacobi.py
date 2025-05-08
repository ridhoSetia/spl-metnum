def print_matrix(mat, name="Matrix"):
    print(f"\n{name}:")
    for row in mat:
        print(["{0:8.4f}".format(x) for x in row])
        
def jacobi(a, b, tol=1e-6, max_iter=100):
    x, y, z = 0.0, 0.0, 0.0

    for itr in range(max_iter):
        x_new = (b[0] - a[0][1]*y - a[0][2]*z) / a[0][0]
        y_new = (b[1] - a[1][0]*x - a[1][2]*z) / a[1][1]
        z_new = (b[2] - a[2][0]*x - a[2][1]*y) / a[2][2]

        print(f"\nIterasi ke-{itr+1}:")
        print(f"x = ( {b[0]} - {a[0][1]}*{y:.6f} + {a[0][2]}*{z:.6f} ) / {a[0][0]} = {x_new:.6f}")
        print(f"y = ( {b[1]} - {a[1][0]}*{x:.6f} + {a[1][2]}*{z:.6f} ) / {a[1][1]} = {y_new:.6f}")
        print(f"z = ( {b[2]} - {a[2][0]}*{x:.6f} + {a[2][1]}*{y:.6f} ) / {a[2][2]} = {z_new:.6f}")

        if (abs(x_new - x) < tol and abs(y_new - y) < tol and abs(z_new - z) < tol):
            print("\nKonvergen. Iterasi dihentikan.")
            break

        x, y, z = x_new, y_new, z_new

    print(f"\nHasil akhir:\nx = {x:.6f}\ny = {y:.6f}\nz = {z:.6f}")
    return [x, y, z]