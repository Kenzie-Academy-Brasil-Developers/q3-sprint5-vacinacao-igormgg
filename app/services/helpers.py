from datetime import datetime, timedelta

from app.models.exceptions_model import InvalidCPF, WrongValueType

def Analize_errors(Vaccine_Cards_Model, data):
    for key in Vaccine_Cards_Model.available_keys:
            if key not in list(data.keys()):
                raise KeyError

    for value in list(data.values()):
        if type(value) != str:
            raise WrongValueType
    
    if len(data['cpf']) != 11:
        raise InvalidCPF

def data_to_post(data):
    new_data = {}

    new_data['cpf'] = data['cpf']
    new_data['name'] = data['name'].title()
    new_data['first_shot_date'] = datetime.utcnow()
    new_data['second_shot_date'] = datetime.utcnow() + timedelta(days=90)
    new_data['vaccine_name'] = data['vaccine_name'].title()
    new_data['health_unit_name'] = data['health_unit_name'].title()

    return new_data