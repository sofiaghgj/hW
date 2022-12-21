import json


def load_candidates() -> list[dict[str, int | str]]:
    with open('candidates.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_candidate(candidate_id):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    candidates = load_candidates()
    people = []
    for i in candidates:
        if candidate_name.lower() in i['name'].lower():
            people.append(i)
    print(people)
    return people


def get_by_skill(skill_name):
    candidate = load_candidates()
    text = []
    for i in candidate:
        if skill_name.lower() in i['skills'].lower():
            text.append(i)
    return text
