from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def cargar_respuestas():
    with open('respuestas.json', 'r') as f:
        return json.load(f)

@app.route('/chat', methods=['GET'])
def chat():
    pregunta = request.args.get('msg', '').lower()
    respuestas = cargar_respuestas()
    respuesta = respuestas.get(pregunta, "No entiendo esa pregunta, pero sigo aprendiendo.")
    return jsonify({"bot": respuesta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

