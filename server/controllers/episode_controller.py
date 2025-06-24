from flask import Blueprint, jsonify
from server.config import db
from server.models.episode import Episode
from flask_jwt_extended import jwt_required

bp = Blueprint('episodes', __name__)

@bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    return jsonify(episode.to_dict())

@bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    db.session.delete(episode)
    db.session.commit()
    return '', 204