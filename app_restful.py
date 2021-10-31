from flask import Flask, request
from flask_restful import Resource, Api
import json

from habilidades import Habilidades, Habilidade

app = Flask(__name__)
api = Api(app)

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
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            menssagem = "Nenhum registro encontrado."
            response = {"status": "erro", "menssagem": menssagem}
        except Exception:
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            response = {"status": "erro", "menssagem": menssagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return {"desenvolvedor": desenvolvedores[id]}

    def delete(self, id):
        dados = json.loads(request.data)
        desenvolvedores.pop(id)
        return  {"status": "sucesso", "menssagem": "Registro excluído"}

#Retorna todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Habilidade, '/habilidades/<int:id>')

if __name__=='__main__':
    app.run(debug=True)