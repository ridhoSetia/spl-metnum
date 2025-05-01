from flask import Flask, render_template, request
from metode import eliminasi_gauss, gauss_jordan, dekomposisi_lu, matriks_balikan, lelaran_jacobi, lelaran_gauss_seidel
import io
import sys

app = Flask(__name__)

# Default
DEFAULT_A = [
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 3]
]
DEFAULT_B = [15, 10, 10]

def capture_output(func, *args):
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        func(*args)
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue()

@app.route('/', methods=['GET', 'POST'])
def index():
    # baca A dan B dari form, atau pakai default
    A = [[None]*3 for _ in range(3)]
    B = [None]*3
    for i in range(3):
        for j in range(3):
            key = f"a_{i}_{j}"
            A[i][j] = int(request.form.get(key, DEFAULT_A[i][j]))
        B[i] = int(request.form.get(f"b_{i}", DEFAULT_B[i]))

    metode = request.form.get("metode", "")
    hasil = ""

    if metode == "Eliminasi Gauss":
        hasil = capture_output(eliminasi_gauss.gauss_elimination, [row[:] for row in A], B[:])
    elif metode == "Gauss Jordan":
        hasil = capture_output(gauss_jordan.gauss_jordan, [row[:] for row in A], B[:])
    elif metode == "Dekomposisi Lu":
        hasil = capture_output(dekomposisi_lu.lu_decomposition, [row[:] for row in A], B[:])
    elif metode == "Matriks Balikan":
        hasil = capture_output(matriks_balikan.inverse_solve, [row[:] for row in A], B[:])
    elif metode == "Lelaran Jacobi":
        hasil = capture_output(lelaran_jacobi.jacobi, [row[:] for row in A], B[:])
    elif metode == "Lelaran Gauss Seidel":
        hasil = capture_output(lelaran_gauss_seidel.gauss_seidel, [row[:] for row in A], B[:])

    return render_template("index.html", hasil=hasil, metode=metode, A=A, B=B)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)