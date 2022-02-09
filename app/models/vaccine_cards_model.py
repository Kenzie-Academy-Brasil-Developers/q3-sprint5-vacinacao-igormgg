from sqlalchemy import Column, String, DateTime
from dataclasses import dataclass

from app.configs.database import db

@dataclass
class Vaccine_Cards_Model(db.Model):
    cpf: str
    name: str
    first_shot_date: str
    second_shot_date: str
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf = Column(String(11), primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

    available_keys = ['cpf', 'name', 'vaccine_name', 'health_unit_name']