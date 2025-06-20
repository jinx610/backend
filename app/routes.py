from flask import Blueprint, request, jsonify
from app import db
from app.models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not name:
        return jsonify({'error': 'name is required'}), 400
    user = User(name=name, email=email)

    print(user)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': f'User {name} created'}), 201

@main_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name} for u in users])
