from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)
api = Api(app)

cred = credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://flask-fab39-default-rtdb.asia-southeast1.firebasedatabase.app/'})

db_ref = db.reference('/flats')

class FlatResource(Resource):
    def get(self, flat_id):
        flat = db_ref.child(flat_id).get()
        if flat:
            return {'flat_id': flat_id, 'data': flat}
        else:
            return {'error': 'Flat not found'}, 404

    def post(self, flat_id):
        json_data = request.get_json()
        if not json_data or 'name' not in json_data or 'price' not in json_data or 'images' not in json_data:
            return {'error': 'Invalid request data'}, 400

        new_flat_data = {
            'name': json_data['name'],
            'price': json_data['price'],
            'images': json_data['images']
        }
        db_ref.child(flat_id).set(new_flat_data)
        return {'flat_id': flat_id, 'data': new_flat_data}, 201  # 201 Created status

class FlatsListResource(Resource):
    def get(self):
        all_flats = db_ref.get(shallow=False)
        # all_flats = db_ref.get(shallow=True)
        return {'data': all_flats}

api.add_resource(FlatResource, '/flat/<flat_id>')
api.add_resource(FlatsListResource, '/flats')

if __name__ == '__main__':
    app.run(debug=True)

...
db.reference("/").update({"language": "python"})
db.reference("/titles").push().set("create modern ui in python")
# transaction
def increment_transaction(current_val):
    return current_val + 1

db.reference("/title_count").transaction(increment_transaction)
ref.get()

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

databaseReference = db.reference("/")
snapshot = databaseReference.child("Bot Applications").order_by_child("status").equal_to("ACTIVE").limit_to_first(self.applicationKeyCollectionCount).get(etag=False, shallow=True)
...
