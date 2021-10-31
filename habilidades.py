from flask import request
from flask_restful import Resource
import json
lista_habilidades = ['Python', 'Flask', 'Django', 'JavaScript', 'TypeScript', 'React Native', 'Reac', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados['habilidade'])
        return lista_habilidades

class Habilidade(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            menssagem = "Nenhum registro encontrado."
            response = {"status": "erro", "menssagem": menssagem}
        except Exception:
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            response = {"status": "erro", "menssagem": menssagem}
        return response

    def put(self, id):
        try:
            dados = json.loads(request.data)
            lista_habilidades[id] = dados['habilidade']
            response = {"status": "Ok", "menssagem": "Registro alterado."}
        except IndexError:
            menssagem = "Nenhum registro encontrado na posição {}.".format(id)
            response = {"status": "erro", "menssagem": menssagem}
        except Exception:
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            response = {"status": "erro", "menssagem": menssagem}
        return response

    def delete(self, id):
        try:
            lista_habilidades.pop(id)
            response =  {"status": "sucesso", "menssagem": "Registro excluído"}
        except IndexError:
            menssagem = "Nenhum registro encontrado na posição {}.".format(id)
            response = {"status": "erro", "menssagem": menssagem}
        except Exception:
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            response = {"status": "erro", "menssagem": menssagem}
        return response