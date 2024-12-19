from models import login_db, UserLogin

def register_authenticate(userid, password):
    exitistinguser = UserLogin.query.filter_by(userid=userid).first()
    if exitistinguser:
        return False
    user = UserLogin(userid=userid, password=password)
    login_db.session.add(user)
    login_db.session.commit()
    return True

def authenticate(userid, password):
    user = UserLogin.query.filter_by(userid=userid).first()
    if user and user.password == password:
        return user
