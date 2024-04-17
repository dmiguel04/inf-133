
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"

@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["GET"])
def sumar():
    num1=int(request.args.get("num1")) 
    num2=int(request.args.get("num2"))
    if not num1 and num2:
        return (
            jsonify({"error": "Se requiere los numeros en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡La suma es = {num1+num2}!"})


@app.route("/palindromo", methods=["GET"])
def palindromo():
    palabra=request.args.get("palabra")
    if not palabra:
        return (
            jsonify({"error": "Se requiere la palabra en los parámetros de la URL."}),
            400,
        )
    if palabra==palabra[::-1]:
        return jsonify({"mensaje": f"¡La palabra {palabra} es palindromo!"})
    else:
        return jsonify({"mensaje": f"¡La palabra {palabra} no es palindromo!"})

if __name__ == "__main__":
    app.run()