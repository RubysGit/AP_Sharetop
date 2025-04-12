from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column
from app import db


class token_data():
    token: str
    data_source: str
    status: int

    def __init__(self, token: str, data_source: str, status: int):
        self.token = token
        self.data_source = data_source
        self.status = status
        return
    

class User(db.Model, UserMixin):
    # from guacamole_entity
    __tablename__ = "guacamole_entity"
    name: Mapped[str] = mapped_column(unique=True, primary_key=True)
    entity_id: Mapped[str] = mapped_column(unique=True)
    type: Mapped[str] = mapped_column()

    def get_id(self):
        return str(self.entity_id)
