from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from app.exc.vacinne_exc import InvalidCpfError
from app.models.vaccine_cards_modles import Vaccines_card
from app.configs.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query





def create_vacinnes_card():
    data = request.get_json()

    data_copy = data.copy()

    for key, value in data_copy.items():
        if key not in ["cpf","name","vaccine_name","health_unit_name"]:
            data.pop(key)


    keys = []
    for key, value in data.items():
        keys.append(key)
        if type(value) != type(""):
            return   {
                "msg":"Valores Invalido",
                "exemple":{
                "cpf": "string",
                "name": "string",
                "vaccine_name": "string",
                "health_unit_name": "string"}

                }, 400

    if sorted(keys) != sorted(["cpf","name","vaccine_name","health_unit_name"]):
            return {
                "msg":"Chaves Invalidas",
                "exemple":{
                "cpf": "string (12345678910)",
                "name": "string",
                "vaccine_name": "string",
                "health_unit_name": "string"}}, 400

    session:Session = db.session

    try:
        new_vacine = Vaccines_card(**data)
    except InvalidCpfError:
        return {
            "msg":"CPF invalido, deve conteer apenas 9 caracters numericos.",
            "exemple":"01234567891"
            },400
    except ValueError:
        return {
            "msg":"CPF invalido, deve conteer apenas 9 caracters numericos.",
            "exemple":"01234567891"
            },400

    try:
        session.add(new_vacine)
        session.commit()
    except IntegrityError:
        return {"msg":"CPF já cadastrado"}, 409
    
    
    return jsonify(new_vacine), 200

def retrive_vaccine_card():

    base_query: Query = db.session.query(Vaccines_card)
    
    records = base_query.all()

   
    return jsonify(records), 200
    
