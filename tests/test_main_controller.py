import json
from controllers.main_controller import MainController


def test_generate_output_level1_success():
    INPUT_FILE = 'data/level1.json'
    OUTPUT_FILE = 'tests/mock/output1.json'

    with open(INPUT_FILE) as f:
        input_data = json.loads(f.read())

        controller = MainController(input_data=input_data, level=1)
        output_generated = controller.generate_output()

        with open(OUTPUT_FILE) as f:
            output_mocked = json.loads(f.read())

            assert output_generated == output_mocked


def test_generate_output_level2_success():
    INPUT_FILE = 'data/level2.json'
    OUTPUT_FILE = 'tests/mock/output2.json'

    with open(INPUT_FILE) as f:
        input_data = json.loads(f.read())

        controller = MainController(input_data=input_data, level=2)
        output_generated = controller.generate_output()

        with open(OUTPUT_FILE) as f:
            output_mocked = json.loads(f.read())

            assert output_generated == output_mocked


def test_generate_output_level3_success():
    INPUT_FILE = 'data/level3.json'
    OUTPUT_FILE = 'tests/mock/output3.json'

    with open(INPUT_FILE) as f:
        input_data = json.loads(f.read())

        controller = MainController(input_data=input_data, level=3)
        output_generated = controller.generate_output()

        with open(OUTPUT_FILE) as f:
            output_mocked = json.loads(f.read())

            assert output_generated == output_mocked


def test_generate_input_level1_output_level2_fail():
    INPUT_FILE = 'data/level1.json'
    OUTPUT_FILE = 'tests/mock/output2.json'
    
    with open(INPUT_FILE) as f:
        input_data = json.loads(f.read())

        controller = MainController(input_data=input_data, level=1)
        output_generated = controller.generate_output()

        with open(OUTPUT_FILE) as f:
            output_mocked = json.loads(f.read())

            assert output_generated != output_mocked

def test_generate_input_level2_output_level3_fail():
    INPUT_FILE = 'data/level2.json'
    OUTPUT_FILE = 'tests/mock/output3.json'
    
    with open(INPUT_FILE) as f:
        input_data = json.loads(f.read())

        controller = MainController(input_data=input_data, level=2)
        output_generated = controller.generate_output()

        with open(OUTPUT_FILE) as f:
            output_mocked = json.loads(f.read())

            assert output_generated != output_mocked