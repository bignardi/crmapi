from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import curso_schema
from ..entidades import curso
from .. services import curso_service
from api import api

class Cursos(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)

        return make_response(cs.jsonify(cursos), 200)

    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]

            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            resultado = curso_service.cadastrar_curso((novo_curso))

            return make_response(cs.jsonify(resultado), 201)

class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso não encontrado."), 404)

        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso), 200)

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Cursos, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')