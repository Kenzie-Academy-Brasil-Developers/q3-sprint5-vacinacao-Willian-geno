from flask import Blueprint
from app.controllers import vacines_controller 

bp = Blueprint("vacinas", __name__, url_prefix=("/vacinas"))

bp.post("")(vacines_controller.create_vacinnes_card)
bp.get("")(vacines_controller.retrive_vaccine_card)