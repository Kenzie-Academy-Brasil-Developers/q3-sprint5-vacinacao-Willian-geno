import string
from flask import jsonify, request, session
from sqlalchemy.exc import IntegrityError
import sqlalchemy 
from app.models.vaccine_cards_modles import Vaccines_card
from app.configs.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query




def create_vacinnes_card():
    data = request.get_json()

    for _, value in data.items():
        if type(value) != type(""):
            return   {
                "mdg":"Valores Invalido",
                "exemple":{
                "cpf": "string",
                "name": "string",
                "vaccine_name": "string",
                "health_unit_name": "string"}

                }, 400

    if data.keys() != ["cpf","name","vaccine_name","health_unit_name"]:
            return {
                "mdg":"Keys Invalido",
                "exemple":{
                "cpf": "string",
                "name": "string",
                "vaccine_name": "string",
                "health_unit_name": "string"}}, 200

    session:Session = db.session

    new_vacine = Vaccines_card(**data)


    try:
        session.add(new_vacine)
        session.commit()
    except IntegrityError:
        return {"msg":"CPF já cadastrado"}, 400
    
    
    return jsonify(new_vacine), 200

def retrive_vaccine_card():

    base_query: Query = db.session.query(Vaccines_card)
    
    records = base_query.all()

   
    return jsonify(records), 200
    
