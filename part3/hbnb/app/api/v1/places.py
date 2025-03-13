from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True,
                             description='Latitude of the place'),
    'longitude': fields.Float(required=True,
                              description='Longitude of the place')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @api.doc(security="token")
    @jwt_required()
    def post(self):
        """Register a new place"""
        current_user = get_jwt_identity()
        data = api.payload
        data['owner_id'] = current_user['id']
        try:
            new_place = facade.create_place(data)
            return {
                'id': new_place.id,
                'message': 'Place successfully created'
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except TypeError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        try:
            places = facade.get_all_places()
            return [place.to_dict() for place in places], 200
        except ValueError as e:
            return {'error': str(e)}, 400


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    @jwt_required()
    @api.doc(security="token")
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.get_place(place_id)
            return place.to_dict(), 200
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @api.doc(security="token")
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        current_user = get_jwt_identity()
        place = facade.get_place(place_id)
        if not place:
            return {'message': 'Invalid input data'}, 400
        if current_user['id'] != place.owner_id:
            return{'error': 'Unauthorized action'}, 403
        try:
            updated_data = api.payload
            updated_data['owner_id'] = current_user['id']
            updated_place = facade.update_place(place_id, updated_data)
            if not updated_place:
                return {'message': 'Place not found'}, 404
            
            return {
                    'id': updated_place.id,
                    'message': 'Place successfully updated'
                }, 200
        except ValueError as e:
            return {'error': str(e)}, 400
        except KeyError as e:
            return {'error': str(e)}, 400
