import json

def read_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    data = read_data_from_json('data.json')
    print("Name:", data['name'])
    print("Age:", data['age'])
    return

def hello_world():
    print("Hello")

if __name__ == "__main__":
    main()