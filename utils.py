import json


def json_list_loader():
    with open('candidates.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


result = json_list_loader()
print(result[0]['name'], result[0]['position'], result[0]['skills'])