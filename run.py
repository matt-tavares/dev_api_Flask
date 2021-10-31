from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Matheus',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1,
        'nome': 'Alex',
        'habilidades': ['Javascript', 'React']
    },
    {
        'id': 2,
        'nome': 'Joana',
        'habilidades': ['C#', '.Net Core']
    }
]

# Retorna, altera e deleta um desenvolveodr pelo ID
@app.route("/dev/<int:id>", methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            menssagem = '"Nenhum registro encontrado."'
            response = {"status": "erro", "menssagem": menssagem}
        except Exception:
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            response = {"status": "erro", "menssagem": menssagem}
        return jsonify(response)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"status": "sucesso", "menssagem": "Registro excluído"})

#Retorna todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route("/dev/", methods=["POST", "GET"])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'menssagem': 'Registro inserido'})
    elif request.method == 'GET':
        return jsonify({"desenvolvedores": desenvolvedores})

if __name__=='__main__':
    app.run(debug=True)