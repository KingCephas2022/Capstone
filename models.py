from datetime import datetime
from extentions import db
from werkzeug.security import generate_password_hash, check_password_hash
from alembic import op
import sqlalchemy as sa

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('urls', lazy=True))
    clicks = db.Column(db.Integer, default=0)  # Add the 'clicks' column
    referrers = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def __init__(self, original_url, short_url, user_id=None):
        self.original_url = original_url
        self.short_url = short_url
        self.user_id = user_id    

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)


# Upgrade function to apply the migration
def upgrade():
    op.add_column('url', sa.Column('created_at', sa.DateTime(), nullable=False))


# Downgrade function to revert the migration
def downgrade():
    op.drop_column('url', 'created_at')

    
