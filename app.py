from flask import Flask, g, session, redirect, url_for
from flask_migrate import Migrate

from exts import db, mail
from blueprints.user import bp as user_bp
from blueprints.qa import bp as qa_bp
from models import UserModel
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrage = Migrate(app, db)

app.register_blueprint(user_bp)
app.register_blueprint(qa_bp)


@app.before_request
def before_request():
    userId = session.get('user_id')
    if userId:
        user = UserModel.query.get(userId)
        g.user = user
    else:
        g.user = None


if __name__ == '__main__':
    app.run()
