from flask import request, current_app, jsonify
from sqlalchemy.exc import IntegrityError

from app.models.exceptions_model import InvalidCPF, WrongValueType
from app.models.vaccine_cards_model import Vaccine_Cards_Model
from app.services.helpers import Analize_errors, data_to_post

def create_vaccine_card():
    data = request.get_json()
    missing_keys = list(set(Vaccine_Cards_Model.available_keys - data.keys()))

    try:

        Analize_errors(Vaccine_Cards_Model, data)

        new_vaccine_card = Vaccine_Cards_Model(**data_to_post(data))


        current_app.db.session.add(new_vaccine_card)
        current_app.db.session.commit()

        return jsonify(new_vaccine_card), 201
    
    except IntegrityError:
        return {'error': f'cpf {data["cpf"]} already exists on database'}, 409
    
    except KeyError:
        return {
            "keys_to_register": Vaccine_Cards_Model.available_keys,
            "missing_keys": missing_keys
        }, 400
    
    except InvalidCPF as err:
        return err.description, err.code
    
    except WrongValueType as err:
        return err.description, err.code

def get_vaccine_cards():
    vaccine_cards = Vaccine_Cards_Model.query.all()

    return jsonify(vaccine_cards)