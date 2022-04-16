from dataclasses import dataclass
from email.policy import default
from tokenize import String
from turtle import st
from app.configs.database import db
from sqlalchemy import BigInteger, Column, Integer, String, DateTime, BIGINT
import datetime as dt

@dataclass
class Vaccines_card(db.Model):
    
    data_atual = dt.datetime.utcnow()
    data_future = data_atual + dt.timedelta(days=90)

    cpf:str
    name:str
    first_shot_date:str
    vaccine_name:str
    health_unit_name:str

    __tablename__= "vaccine_cards"

    cpf= Column(String(11),primary_key=True) 
    name= Column(String,nullable=False)
    first_shot_date= Column(DateTime, default=data_atual)
    second_shot_date= Column(DateTime, default=data_future)
    vaccine_name= Column(String, nullable=False)
    health_unit_name= Column(String)
    
    def __repr__(self) -> str:
        return f"{self.cpf} - [{self.name}] -> [{self.first_shot_date}]"