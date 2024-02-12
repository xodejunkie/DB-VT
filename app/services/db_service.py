from app.models.sql_models import db, User

def create_user(username):
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()

def get_user(user_id):
    return User.query.get(user_id)
