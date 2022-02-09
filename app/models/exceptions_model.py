class InvalidCPF(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = 400
        self.description = {'error': 'CPF must contain 11 characters'}

class WrongValueType(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.code = 400
        self.description = {'error': 'All input types must be strings'}