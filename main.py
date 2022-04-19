from flask import Flask
from utils import load_candidates, reformat_candidates, load_candidate_by_id, load_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def main():
    candidates_list = load_candidates('candidates.json')

    return reformat_candidates(candidates_list)


@app.route("/candidates/<int:candidate_id>")
def page_candidate(candidate_id):

    candidates_list = load_candidates('candidates.json')
    candidate = load_candidate_by_id(candidates_list, candidate_id)
    result = f'<img src="{candidate["picture"]}">'

    return result + reformat_candidates([candidate])


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates_list = load_candidates('candidates.json')

    return reformat_candidates(load_candidates_by_skill(candidates_list, skill))


app.run()
