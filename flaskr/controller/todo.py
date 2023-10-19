from dataclasses import dataclass
from flaskr.repository.todo import TodoRepository
from flaskr.models.todo import Todo


@dataclass
class TodoController:
    todo_repository: TodoRepository

    def create_todo(self, todo: Todo):
        self.todo_repository.insert_todo(todo)

    def get_todos(self):
        return self.todo_repository.get_todos()


