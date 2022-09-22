import string, random
from flask import Blueprint, render_template, request, session,redirect,url_for,jsonify,flash
from flask_mail import Message
from werkzeug.security import generate_password_hash,check_password_hash

from models import UserModel
from .forms import RegisterForm,LoginForm
from exts import mail, db

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    session['user_id'] = user.id
                    return redirect(url_for("qa.index"))
                else:
                    flash("密码错误")
                    return render_template('login.html')
            else:
                flash('该邮箱不存在！')
                return render_template('login.html')
        else:
            flash('请输入6-18位的密码！')
            return redirect(url_for('user.login'))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user.login'))


@bp.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            hash_password = generate_password_hash(password)
            user = UserModel(email=email, username=username, password=hash_password)

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return render_template('register.html')

@bp.route('/mail',methods=['POST','GET'])
def send_email():
    captcha_code = "".join(random.sample(string.ascii_letters + string.digits, 4))
    session['captcha'] = captcha_code
    email = request.form.get('email')
    if mail:
        message = Message(
            subject="验证码",
            recipients=[email],
            body=f'【项目】您的验证码为：{captcha_code}。'
        )
        mail.send(message)
        return jsonify({"code": 200})
    else:
        return jsonify({"code":400,"message":"请输入邮箱"})
