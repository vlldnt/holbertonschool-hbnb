from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True,
                             description='Latitude of the place'),
    'longitude': fields.Float(required=True)
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        data = api.payload
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
    def put(self, place_id):
        """Update a place's information"""
        data = api.payload
        try:
            updated_place = facade.update_place(place_id, data)
            return {
                'id': updated_place.id,
                'message': 'Place successfully updated'
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 404
        except TypeError as e:
            return {'error': str(e)}, 400