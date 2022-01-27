from sqlalchemy import Column, Integer, String

from .database import Base

#local test database

class User(Base):
    __tablename__ = "login"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def get_display_name(self) -> str:
        return self.name if self.name is not None else self.login