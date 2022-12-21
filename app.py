from flask import Flask, request, render_template
from utils import *

app = Flask(__name__)

@app.route("/")
def hello():
    candidates = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:x>")
def single(x):
    candidate = get_candidates_by_name(x)
    candi = load_candidates()
    name = candi["name"]
    position = candi["position"]
    skills = candi["skills"]
    picture = candi["picture"]
    return render_template('single.html',candidate=candidate)

# @app.route("/search/<candidate_name>")
# def search(candidate_name):
#         candi = load_candidates()
#         counter = 0
#         if candidate_name in candi["name"]:
#             counter += 1
#             name = candi["name"]
#             bill = counter
#         return render_template('search.html', name=name,bill=bill)
# @app.route("/skill/<skill_name>")
# def search(skill_name):
#         candi = get_by_skill(skill_name)
#         counter = 0
#         if candidate_name in candi["name"]:
#             counter += 1
#             name = candi["name"]
#             bill = counter
#         return render_template('search.html', name=name,bill=bill)
#
# @app.route("/skills/<x>")
# def skills(x):
#         skill = get_by_skill(x)
#         for i in skill:
#             name = i["name"]
#         return render_template('skill.html', name=name,)
#
#
#
#
#
#
#
#
#
#
# @app.route("/candidates/<int:x>")
# def single(x):
#     candi = get_candidates_by_name(x)
#
#
#     url = "http://mypictures.me/200"
#     inform = f'<img src="{candi["picture"]}">\n<pre>Имя кандидата - {candi["name"]}\nПозиция кандидата - {candi["position"]}\nНавыки - {candi["skills"]}</pre>\n'
#     return inform
#
# @app.route("/skills/<x>")
# def skills(x):
#         skill = get_by_skill(x)
#         text = ''
#         for i in skill:
#             text += f'<pre>Имя кандидата - {i["name"]}\n{i["position"]}\n{i["skills"]}'
#         return text
#
# app.run()
#
# def main(list_can):
#     sym = ''
#     for i in range(len(list_can)):
#         sym += f'''
#         Имя кандидата - {list_can[i]['name']}
#         Позиция кандидата {list_can[i]['position']}
#         Навыки' {list_can[i]['skills']}
#         '''
#     return f'<pre>{sym}</pre>'
#
# @app.route("/")
# def page_index():
#     return main(load_candidates())

app.run()
