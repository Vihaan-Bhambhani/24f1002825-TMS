import os
from werkzeug.security import generate_password_hash
from extensions import db
from models import User


def seed_admin():
    #Create the admin user if one doesn't already exist.
    existing_admin = User.query.filter_by(role='admin').first()

    if existing_admin is None:
        admin = User(
            name='Admin',
            email=os.environ.get('ADMIN_EMAIL', 'admin@example.com'),
            password_hash=generate_password_hash(os.environ.get('ADMIN_PASSWORD') or 'local-development-only-change-me'),
            role='admin',
            is_active=True,
            is_blacklisted=False
        )
        db.session.add(admin)
        db.session.commit()
        print('[OK] Admin user created')
    else:
        print('[OK] Admin user already exists, skipping seed')
