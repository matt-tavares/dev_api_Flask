from flask import request, Response
from flask_restful import Resource
import json
lista_habilidades = ['Python', 'Flask', 'Django', 'JavaScript', 'TypeScript', 'React Native', 'React', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades, 200

    def post(self):
        try:
            dados = json.loads(request.data)
            dadoInLista = dados['habilidade'] in lista_habilidades
            if dadoInLista:
                status = "erro"
                menssagem = "Registro já existente."
                code = 400
            else:
                lista_habilidades.append(dados['habilidade'])
                status = "Ok"
                menssagem = "Registro adicionado."
                code = 201
        except:
            status = "erro"
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            code = 400
        return {"status": status, "menssagem": menssagem}, code

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
        return Response(response, status=200, mimetype='application/json')

    def put(self, id):
        try:
            dados = json.loads(request.data)
            code = 200
            lista_habilidades[id] = dados['habilidade']
            response = {"status": "Ok", "menssagem": "Registro alterado."}
        except IndexError:
            code = 406
            menssagem = "Nenhum registro encontrado na posição {}.".format(id)
            response = {"status": "erro", "menssagem": menssagem}
        except Exception:
            code = 400
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            response = {"status": "erro", "menssagem": menssagem}
        return response, code

    def delete(self, id):
        try:
            lista_habilidades.pop(id)
            code = 200
            response =  {"status": "sucesso", "menssagem": "Registro excluído"}
        except IndexError:
            code = 406
            menssagem = "Nenhum registro encontrado na posição {}.".format(id)
            response = {"status": "erro", "menssagem": menssagem}
        except Exception:
            code = 400
            menssagem = "Erro desconhecido. Procure o administrador da APi."
            response = {"status": "erro", "menssagem": menssagem}
        return response, code