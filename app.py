from flask import Flask, request, jsonify
from flask_cors import CORS
from banco import inserir_pet, listar_pets

app = Flask(__name__)
CORS(app)

@app.route('/pets', methods=['POST'])
def cadastrar_pet():
    try:
        dados = request.json
        campos_obrigatorios = ["nome", "porte", "idade", "tipo", "localizacao", "imagem"]
        
        for campo in campos_obrigatorios:
            if not dados.get(campo):
                return jsonify({"status": "erro", "mensagem": f"Campo '{campo}' é obrigatório"}), 400

        inserir_pet(dados)
        return jsonify({"status": "sucesso", "mensagem": "Pet cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": f"Erro ao cadastrar pet: {str(e)}"}), 500

@app.route('/pets', methods=['GET'])
def obter_pets():
    try:
        pets = listar_pets()
        return jsonify({"status": 200, "data": pets}), 200
    except Exception as e:
        return jsonify({"status": "erro", "mensagem": f"Erro ao listar pets: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
