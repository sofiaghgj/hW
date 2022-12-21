from flask import Flask, request, render_template
from utils import *

app = Flask(__name__)


@app.route("/")
def main_page():
    info = load_candidates()
    return render_template('list.html', info=info)


@app.route("/candidate/<int:x>")
def single(x):
    info = get_candidate(x)
    return render_template('single.html', info=info)


@app.route("/search/<candidate_name>")
def search(candidate_name):
    info = get_candidates_by_name(candidate_name)
    print(info)
    return render_template('search.html', info=info, bill=len(info))


@app.route("/skill/<skill_name>")
def skills(skill_name):
    info = get_by_skill(skill_name)
    print(info)
    return render_template('skill.html', info=info, bill=len(info), skill_name=skill_name)

"""@app.route("/skill/<skill_name>")
def search(skill_name):
        candi = get_by_skill(skill_name)
        counter = 0
        if skill_name in candi["name"]:
            counter += 1
            name = candi["name"]
            bill = counter
        return render_template('search.html', name=name,bill=bill)"""




app.run()
