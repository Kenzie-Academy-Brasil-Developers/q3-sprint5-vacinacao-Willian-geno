from dataclasses import dataclass
from tokenize import String
from turtle import st
from app.configs.database import db
from sqlalchemy import BigInteger, Column, Integer, String, DateTime, BIGINT

@dataclass
class Vaccines_card(db.Model):

    id: bool
    cpf:str
    name:str
    first_shot_date:str
    vaccine_name:str
    health_unit_name:str

    __tablename__= "vaccine_cards"

    id= Column(BigInteger, primary_key=True)
    cpf= Column(String(11)) 
    name= Column(String,nullable=False)
    first_shot_date= Column(DateTime)
    second_shot_date= Column(DateTime)
    vaccine_name= Column(String, nullable=False)
    health_unit_name= Column(String)
    
    def __repr__(self) -> str:
        return f"{self.id} - [{self.name}] -> [{self.first_shot_date}]"