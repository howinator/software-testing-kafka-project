import json


def get_test_cases():
    return [get_test_case(i) for i in range(1)]


def get_test_case(test_number):
    return get_file_locally(f"test_{test_number}")


def get_file_locally(file_name):
    with open(f"../{file_name}.json") as f:
        return json.load(f)
