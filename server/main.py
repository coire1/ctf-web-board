import os
from flask import Flask, send_file
from flask import request
from flask_cors import CORS
import models as dbHandler
from flask import jsonify


APP_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(APP_DIR)
DIST_DIR = os.path.join(ROOT_DIR, '../client/dist')

app = Flask(__name__,  static_url_path='')
CORS(app)

if not os.path.exists(DIST_DIR):
    raise Exception(
        'DIST_DIR not found: {}'.format(DIST_DIR))


@app.route('/', methods=['POST', 'GET'])
def home():
    entry = os.path.join(DIST_DIR, 'index.html')
    return send_file(entry)


@app.route('/api/challenges')
def get_challenges():
    challenges = dbHandler.getChallenges()
    return jsonify(challenges)


@app.route('/api/challenges/<challenge_id>')
def get_challenge_rank(challenge_id):
    challenge = dbHandler.getChallenge(challenge_id)
    return jsonify(challenge)


@app.route('/api/challenges/<challenge_id>/rank')
def get_challenge(challenge_id):
    challenge = dbHandler.getChallengeRank(challenge_id)
    return jsonify(challenge)


@app.route('/api/challenges/<challenge_id>', methods=['POST'])
def check_challenge(challenge_id):
    response = {}
    values = request.get_json()
    if (values):
        key = values['key']
        username = values['username']
        response = dbHandler.checkChallenge(
            challenge_id, key, username
        )
    return jsonify(response)


@app.route('/api/rank')
def get_rank():
    users = dbHandler.getRank()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
