from flask import Blueprint, jsonify
from app.util.errors import CustomError

api_bp = Blueprint('api', __name__)

@api_bp.app_errorhandler(CustomError)
def handle_custom_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
