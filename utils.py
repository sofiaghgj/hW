import json

def load_candidates_from_json(file) -> list[dict[str, int | str]]:
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_candidates():
    return load_candidates_from_json('candidates.json')


def get_candidate(candidate_id):
    candidates = load_candidates()
    for i in candidates:
        if i['id'] == candidate_id:
            return i


def get_candidates_by_name(candidate_name):
    candidat = load_candidates()
    for i in candidat:
        if i['name'] == candidate_name:
            return i


def get_by_skill(skill_name):
    candidat = load_candidates()
    text = []
    for i in candidat:
        if skill_name.lower() in i['skills'].lower():
            text.append(i)
    return text








