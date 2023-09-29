from flask import request, jsonify
from flask_jwt_extended import create_access_token

from app.models.user import User
from app.util.errors import CustomError
from app.routes import api_bp

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        raise CustomError('Invalid username or password', status_code=401)

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)
