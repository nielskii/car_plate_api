from flask import Flask,render_template,request,jsonify
from api_plate import fetch_data


app = Flask(__name__)

@app.route("/search")
def search_plate():
    query = request.args.get('p', "")
    result = fetch_data(query)
    if result:
        print(f'Dados encontrados: {result}')
        return jsonify({'data':result}),200
    else:
        print('Nenhum dado encontrado ou placa inválida', 400)


if __name__ == "__main__":
    app.run(debug=True)
