import wtforms
from wtforms.validators import email, length, EqualTo
from flask import session


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    username = wtforms.StringField(validators=[length(min=6, max=20)])
    password = wtforms.StringField(validators=[length(min=6, max=18)])
    password_confirm = wtforms.StringField(validators=[EqualTo('password')])

    def validate_captcha(self, field):
        captcha = field.data
        session_captcha = session.get('captcha')
        if not captcha.upper() == session_captcha.upper():
            raise wtforms.ValidationError('验证码错误！')


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=18)])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=1,max=200)])
    content = wtforms.StringField(validators=[length(min=1)])


class AnswerForm(wtforms.Form):
    answer_content = wtforms.StringField(validators=[length(min=1)])
