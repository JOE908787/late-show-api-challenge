from server.config import db, app
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date

def seed_data():
    db.drop_all()
    db.create_all()

    # Seed Users
    user1 = User(username='admin')
    user1.set_password('password')
    db.session.add(user1)

    # Seed Guests
    g1 = Guest(name='John Doe', occupation='Actor')
    g2 = Guest(name='Jane Smith', occupation='Comedian')
    db.session.add_all([g1, g2])

    # Seed Episodes
    e1 = Episode(date=date(2025, 6, 1), number=1)
    e2 = Episode(date=date(2025, 6, 2), number=2)
    db.session.add_all([e1, e2])

    db.session.commit()

    # Seed Appearances
    a1 = Appearance(rating=4, guest_id=g1.id, episode_id=e1.id)
    a2 = Appearance(rating=5, guest_id=g2.id, episode_id=e1.id)
    a3 = Appearance(rating=3, guest_id=g1.id, episode_id=e2.id)
    db.session.add_all([a1, a2, a3])

    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()