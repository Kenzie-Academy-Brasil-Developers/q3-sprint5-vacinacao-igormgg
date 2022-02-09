from flask import Flask, Blueprint

from app.routes.vaccine_card_route import bp_vaccine_cards

def init_app(app: Flask):
    app.register_blueprint(bp_vaccine_cards)