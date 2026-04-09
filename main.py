from flask import Flask, render_template, request, jsonify
from api_plate import fetch_data
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "API Online", "mensagem": "Car Plate API operante"}), 200

@app.route("/search")
def search_plate():
    # .strip() evita que um espaco no final da URL quebre a busca
    query = request.args.get('p', "").strip()
    
    if not query:
        return jsonify({'error': 'Parametro p (placa) e obrigatorio'}), 400

    try:
        result = fetch_data(query)
        if result:
            return jsonify({'data': result}), 200
        else:
            return jsonify({'error': 'Placa nao encontrada ou erro na raspagem'}), 404
            
    except Exception as e:
        # Se der erro no scraper (ex: falta de Node.js), a API vai te avisar aqui
        return jsonify({
            'error': 'Erro interno ao processar a busca',
            'details': str(e)
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)