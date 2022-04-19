import json


def load_candidates(path):
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)
