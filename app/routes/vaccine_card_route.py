from flask import Blueprint

from app.controllers.vaccine_cards_controller import create_vaccine_card, get_vaccine_cards

bp_vaccine_cards = Blueprint("bp_vaccine_card", __name__, url_prefix="/vaccinations")

bp_vaccine_cards.post("")(create_vaccine_card)
bp_vaccine_cards.get("")(get_vaccine_cards)