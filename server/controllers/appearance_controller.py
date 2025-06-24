from flask import Blueprint, request, jsonify
from server.config import db
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from flask_jwt_extended import jwt_required

bp = Blueprint('appearances', __name__)

@bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        rating = data['rating']
        guest_id = data['guest_id']
        episode_id = data['episode_id']

        if not Guest.query.get(guest_id):
            return jsonify({'error': 'Guest not found'}), 400
        if not Episode.query.get(episode_id):
            return jsonify({'error': 'Episode not found'}), 400

        appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing key: {e.args[0]}'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400