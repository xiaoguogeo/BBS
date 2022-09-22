from flask import Blueprint, render_template, g, redirect, url_for, request, flash
from sqlalchemy import or_

from decorators import login_required
from models import QuestionModel,AnswerModel
from .forms import QuestionForm,AnswerForm
from exts import db

bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    questions = QuestionModel.query.order_by(db.text("-create_time")).all()
    return render_template('index.html', questions=questions)


@bp.route('/question/public', methods=['POST', 'GET'])
@login_required
def question_public():
    if request.method == 'GET':
        return render_template('question_public.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author_id=g.user.id)
            db.session.add(question)
            db.session.commit()

            return redirect('/')
        else:
            flash("标题和内容不能为空！")
            return redirect(url_for('qa.question_public'))


@bp.route('/detail/<int:question_id>')
def question_detail(question_id):
    question = QuestionModel.query.get(question_id)
    return render_template('detail.html', question=question)


@bp.route('/comment/<int:question_id>',methods=['POST'])
@login_required
def comment(question_id):
    form = AnswerForm(request.form)
    if form.validate():
        answer_content = form.answer_content.data
        author = g.user
        answer = AnswerModel(content=answer_content,author=author,question_id=question_id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.question_detail",question_id=question_id))
    else:
        flash("请输入评论内容！")
        return redirect(url_for("qa.question_detail",question_id=question_id))


@bp.route("/search",methods=['GET'])
def search():
    q=request.args.get('q')
    questions=QuestionModel.query.filter(or_(QuestionModel.title.contains(q),QuestionModel.content.contains(q))).order_by(db.text("-create_time"))
    return render_template('index.html',questions=questions)