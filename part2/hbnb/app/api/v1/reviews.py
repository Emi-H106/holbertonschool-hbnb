from flask_restx import Namespace, Resource, fields
from app.services.facade import facade
from flask import request

api = Namespace("reviews", description="Gestion des avis")

review_model = api.model("Review", {
    "id": fields.String(readonly=True),
    "user_id": fields.String(required=True),
    "place_id": fields.String(required=True),
    "text": fields.String(required=True)
})

@api.route("/")
class ReviewListResource(Resource):
    @api.marshal_list_with(review_model)
    def get(self):
        """List all reviews"""
        return ｆacade.get_all_reviews()

    @api.expect(review_model, validate=True)
    @api.marshal_with(review_model, code=201)
    def post(self):
        """Create a new notice"""
        try:
            return facade.create_review(api.payload), 201
        except ValueError as e:
            api.abort(400, str(e))

@api.route("/<string:review_id>")
@api.param("review_id", "Identifiant de l'avis")
class ReviewResource(Resource):
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Recover a notice by ID"""
        review = facade.get_review(review_id)
        if not review:
            api.abort(404, "Avis non trouvé")
        return review

    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """Update a notice"""
        review = facade.update_review(review_id, api.payload)
        if not review:
            api.abort(404, "Avis non trouvé")
        return review

    def delete(self, review_id):
        """Delete a notification"""
        deleted = facade.delete_review(review_id)
        if not deleted:
            api.abort(404, "Avis non trouvé")
        return {"message": "Avis supprimé"}, 204

@api.route("/place/<string:place_id>")
@api.param("place_id", "Identifiant du lieu")
class PlaceReviewResource(Resource):
    @api.marshal_list_with(review_model)
    def get(self, place_id):
        """List the notices associated with a location"""
        return facade.get_reviews_by_place(place_id)
