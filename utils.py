import json


def load_candidates(path):
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)


def reformat_candidates(candidates_list):
    result = '<pre>'
    for person in candidates_list:
        result += (
            f'Имя кандидата - {person["name"]}\n'
            f'Позиция кандидата - {person["position"]}\n'
            f'Навыки кандидата - {person["skills"]}\n'
            f'\n'
        )
    result += '</pre>'

    return result


def load_candidate_by_id(candidates_list, candidate_id):
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate


def load_candidates_by_skill(candidate_list, candidate_skill):
    result = []

    for candidate in candidate_list:
        candidate_skills = candidate['skills'].lower().split(", ")
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result


