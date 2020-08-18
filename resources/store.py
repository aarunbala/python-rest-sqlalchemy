from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "Store with {} not found".format(name)}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)

        if store is None:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {'message': 'Error occurred when creating Store'}, 500
            return store.json(), 201
        else:
            return {'message': "Store {} already exists".format(name)}, 400

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
        return {'message': "Store {} deleted".format(name)}


class StoreList(Resource):

    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}