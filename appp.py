from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

cred = credentials.Certificate('cred.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

flats_collection = db.collection('flats')

class FirestoreResource(Resource):
    def get(self, document_id):
        doc_ref = flats_collection.document(document_id)
        doc_data = doc_ref.get().to_dict()
        if doc_data:
            return {'document_id': document_id, 'data': doc_data}
        else:
            return {'error': 'Document not found'}, 404

    def post(self, document_id):
        args = request.get_json()

        doc_ref = flats_collection.document(document_id)
        doc_ref.set({
            'name': args['name'],
        })

        return {'document_id': document_id, 'message': 'Document created successfully'}, 201

# Register the Resource with Flask-RESTful
api.add_resource(FirestoreResource, '/flat/<string:document_id>')

# Run the Flask Application
if __name__ == '__main__':
    app.run(debug=True)