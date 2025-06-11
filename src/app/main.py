from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def beranda():
    return "Kalkulator sederhana aktif"

def ambil_argumen():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        return a, b, None
    except ValueError:
        return None, None, "Input tidak valid"

@app.route("/tambah", methods=["GET"])
def tambah():
    a, b, error = ambil_argumen()
    if error:
        return jsonify(error=error), 400
    return jsonify(hasil=a + b)

@app.route("/kurang", methods=["GET"])
def kurang():
    a, b, error = ambil_argumen()
    if error:
        return jsonify(error=error), 400
    return jsonify(hasil=a - b)

@app.route("/kali", methods=["GET"])
def kali():
    a, b, error = ambil_argumen()
    if error:
        return jsonify(error=error), 400
    return jsonify(hasil=a * b)

@app.route("/bagi", methods=["GET"])
def bagi():
    a, b, error = ambil_argumen()
    if error:
        return jsonify(error=error), 400
    if b == 0:
        return jsonify(error="Pembagian dengan nol tidak diperbolehkan"), 400
    return jsonify(hasil=a / b)

if __name__ == "__main__":
    app.run(debug=True)
