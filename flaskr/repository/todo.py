from dataclasses import dataclass
from typing import Sequence, Type
from sqlalchemy import select
from sqlalchemy.orm import (
    Session, scoped_session
)

from flaskr.models.todo import Todo


@dataclass
class TodoRepository:
    session: scoped_session[Session]

    def insert_todo(self, todo: Todo):
        with self.session() as session:
            session.add(todo)
            session.commit()

    def get_todos(self) -> Sequence[Todo]:
        with self.session() as session:
            stmt = select(Todo)
            all_todo = session.scalars(stmt).all()

        return all_todo

    def get_todo(self, id: int) -> Type[Todo]:
        with self.session() as session:
            todo = session.get(Todo, id)

        return todo