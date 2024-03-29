from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from service.decorators import admin_requered, auth_requered

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_requered
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    @admin_requered
    def post(self):
        req_json = request.json
        new_genre = director_service.create(req_json)
        return "", 201, {'location': f"/{director_ns.name}/{new_genre.id}"}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_requered
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_requered
    def put(self, rid):
        req_json = request.json
        if 'id' not in req_json:
            req_json['id'] = rid
        director_service.update(req_json)
        return "", 204

    @admin_requered
    def delete(self, rid):
        director_service.delete(rid)
        return "", 204

