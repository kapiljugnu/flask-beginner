from flask import Blueprint, render_template, request, redirect

from flaskr.models.todo import Todo
from flaskr.repository.todo import TodoRepository
from flaskr.controller.todo import TodoController
from flaskr.db import app_db

todo_dp = Blueprint('todo', __name__)

todo_repository = TodoRepository(app_db.session)
todo_controller = TodoController(todo_repository)


@todo_dp.get('/')
def get_all_todos():
    todos = todo_controller.get_todos()
    return render_template('todo/list.html', todos=todos)


@todo_dp.get('/create')
def render_create_todo():
    return render_template('todo/create.html')


@todo_dp.post('/create')
def create_todo():
    task = request.form['task']
    todo = Todo(task=task)
    todo_controller.create_todo(todo)
    return redirect('/')
