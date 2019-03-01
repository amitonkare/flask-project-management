# from app import app
from flask import current_app, Blueprint, render_template ,request, redirect, url_for
from sqlalchemy.orm import joinedload
from flaskr.models import *
from flaskr.forms import ProjectCreateForm, TaskCreateForm
from flaskr.db import db_session

home = Blueprint('home', __name__, url_prefix='/')
project = Blueprint('project', __name__, url_prefix='/project')
# task = Blueprint('task', __name__, url_prefix='/task')

@home.route('/', methods=['GET'])
def index():
	return render_template("index.html", name="Amit")


@project.route('/', methods=['GET', 'POST'])
def list():
    # query projects
    projects = Project.query.all()
    # projects = Project.query.filter_by(status='active')
    # print(projects)
    return render_template("projects/project_list.html", projects=projects)


@project.route('/create', methods=['GET', 'POST'])
def create():
    form=ProjectCreateForm(request.form)
    if request.method == 'GET':
        return render_template('projects/create_project.html', form=form)
    if request.method == 'POST' and form.validate():
        # print(form.name.data, form.client.data, form.technology.data, form.status.data)
        project = Project(form.name.data, form.client.data, form.technology.data, form.status.data)
        db_session.add(project)
        db_session.commit()
        return redirect(url_for('project.list'))


# @project.route('/details/<int:project_id>', methods=['GET'])
# def details(project_id):
#     project = Project.query.filter(id=project_id).first()
#     # form = ProjectCreateForm(obj=project)
#     return render_template('projects/project_detail.html', project=project)


@project.route('/edit/<int:project_id>', methods=['GET', 'POST'])
def edit(project_id):
    project = Project.query.filter_by(id=project_id).first()
    form = ProjectCreateForm(obj=project)
    if request.method == 'GET':
        return render_template('projects/create_project.html', form=form, edit=1)
    if request.method == 'POST':
        project.name = request.form.get("name")
        project.technology = request.form.get("technology")
        project.client = request.form.get("client")
        project.status = request.form.get("status")
        # print(project.technology)
        db_session.merge(project)
        db_session.commit()
        return redirect(url_for('project.list'))


@project.route('/delete/<int:project_id>', methods=['GET'])
def delete(project_id):
    project = Project.query.filter_by(id=project_id).first()
    current_db_sessions = db_session.object_session(project)
    current_db_sessions.delete(project)
    current_db_sessions.commit()
    return redirect(url_for('project.list'))


@project.route('/<int:project_id>/tasks', methods=['GET'])
def tlist(project_id):
    tasks = Task.query.filter_by(project_id=project_id)
    if tasks.count() > 0:
        # print("Project Name: "+tasks[0].project.name)
        return render_template("tasks/tasks_list.html", tasks=tasks)
    else:
        project = Project.query.filter_by(id=project_id).first()
        return render_template("tasks/tasks_list.html", project=project, tasks=tasks)


@project.route('/<int:project_id>/create_task', methods=['GET', 'POST'])
def tcreate(project_id):
    form = TaskCreateForm(request.form)
    if request.method == 'GET':
        project = Project.query.filter_by(id=project_id).first()
        form.project_id.data = project_id
        return render_template('tasks/create_task.html', form=form, project=project)
    if request.method == 'POST' and form.validate():
        # print("Project ID: ",form.project_id)
        task = Task(title=form.title.data, description=form.description.data, project_id=form.project_id.data)
        db_session.add(task)
        db_session.commit()
        return redirect(url_for('project.tlist', project_id=project_id))


@project.route('/<int:project_id>/edit_task/<int:task_id>', methods=['GET', 'POST'])
def tedit(project_id, task_id):
    task = Task.query.filter_by(id=task_id).first()
    form = TaskCreateForm(obj=task)
    if request.method == 'GET':
        return render_template('tasks/create_task.html', form=form, project=project, edit=1)
    if request.method == 'POST':
        task.title = request.form.get("title")
        task.description = request.form.get("description")
        # print(task.description)
        db_session.merge(task)
        db_session.commit()
        return redirect(url_for('project.tlist', project_id=project_id))


@project.route('<int:project_id>/delete/<int:task_id>', methods=['GET'])
def tdelete(project_id, task_id):
    task = Task.query.filter_by(id=task_id).first()
    current_db_sessions = db_session.object_session(task)
    current_db_sessions.delete(task)
    current_db_sessions.commit()
    return redirect(url_for('project.tlist', project_id=project_id))


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The project page'