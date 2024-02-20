from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.database.db import Database


class User(Database.Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
