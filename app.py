import json

def read_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def print_persons():
    data = read_data_from_json('data.json')
    print("Name:", data['name'])
    print("Age:", data['age'])

def main():
    print_persons()

def hello_world():
    print("Hello")


if __name__ == "__main__":
    main()