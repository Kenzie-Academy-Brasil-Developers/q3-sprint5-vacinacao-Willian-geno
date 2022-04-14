from flask import jsonify, request, session
from app.models.vaccine_cards_modles import Vaccines_card
from app.configs.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import Query



def create_vacinnes_card():
    data = request.get_json()

    session:Session = db.session

    new_vacine = Vaccines_card(**data)

    print("="*100)
    print(data)
    print("="*100)
    print(new_vacine)
    print("="*100)

    session.add(new_vacine)
    session.commit()

    return jsonify(new_vacine), 200

def retrive_vaccine_card():

    base_query: Query = db.session.query(Vaccines_card)
    
    records = base_query.all()

    return jsonify(records), 200
    
