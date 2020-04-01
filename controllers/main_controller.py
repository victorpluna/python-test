import json


class MainController:
    def __init__(self, input_data, level):
        self.input_data = input_data
        self.level = level
    
    def generate_output(self):
        # Temporary code to test the output mocked
        with open(f'mock/output{self.level}.json') as f:
            return json.loads(f.read())