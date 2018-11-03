import sqlite3 as sql
import hashlib
import time


DATABASE_PATH = '../db/database.db'
FLAG_POINTS = 10
BLOOD_POINTS = 30


def getChallenges():
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute("SELECT id, name, address, description FROM challenges")
    challenges = cur.fetchall()
    con.close()
    results = []
    for challenge in challenges:
        results.append(
            {
                'id': challenge[0],
                'name': challenge[1],
                'address': challenge[2],
                'description': challenge[3]
            }
        )
    return results


def getChallenge(challenge_id):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "SELECT id, name, address, description FROM challenges WHERE id=?",
        (int(challenge_id),)
    )
    challenge = cur.fetchone()
    con.close()
    return {
        'id': challenge[0],
        'name': challenge[1],
        'address': challenge[2],
        'description': challenge[3]
    }


def checkChallenge(challenge_id, key, username):
    result = False
    blood = False
    exists = False
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "SELECT id FROM challenges WHERE id=? AND flag=?",
        (
            int(challenge_id),
            hashlib.md5(key.encode('utf8')).hexdigest(),
        )
    )
    challenge = cur.fetchone()
    if (challenge):
        result = True
        cur.execute(
            "SELECT id FROM points WHERE challenge_id=?",
            (int(challenge_id),)
        )
        existingPoints = cur.fetchall()
        if (len(existingPoints) == 0):
            blood = True
        else:
            blood = False
        cur.execute(
            "SELECT id FROM points WHERE challenge_id=? AND username=?",
            (int(challenge_id), str(username),)
        )
        existingUser = cur.fetchall()
        if (len(existingUser) == 0):
            cur.execute(
                "INSERT INTO \
                points(username, challenge_id, created_at, blood) \
                VALUES (?, ?, ?, ?)",
                (str(username), int(challenge_id), time.time(), blood,)
            )
            con.commit()
        else:
            exists = True
    con.close()
    response = {
        "flag": result,
        "blood": blood,
        "exists": exists
    }
    return response


def getRank():
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute("SELECT \
        id, \
        username, \
        (SELECT COUNT(*) FROM points b WHERE a.username = b.username) AS agg_points, \
        (SELECT COUNT(*) FROM points b WHERE a.username = b.username AND b.blood = 1) AS agg_blood \
        FROM points a \
        GROUP BY username \
    ")
    users = cur.fetchall()
    con.close()
    results = []
    for user in users:
        results.append(
            {
                'id': user[0],
                'username': user[1],
                'bloods': user[3],
                'points': (user[3] * BLOOD_POINTS) + (user[2] * FLAG_POINTS)
            }
        )
    return sorted(results, key=lambda k: k['points'], reverse=True)


def getChallengeRank(challenge_id):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute("SELECT \
        id, \
        username, \
        (SELECT COUNT(*) FROM points b WHERE a.username = b.username AND b.challenge_id = ?) AS agg_points, \
        (SELECT COUNT(*) FROM points b WHERE a.username = b.username AND b.blood = 1 AND b.challenge_id = ?) AS agg_blood \
        FROM points a \
        WHERE a.challenge_id = ? \
        GROUP BY username \
    ", (int(challenge_id), int(challenge_id), int(challenge_id),))
    users = cur.fetchall()
    con.close()
    results = []
    for user in users:
        results.append(
            {
                'id': user[0],
                'username': user[1],
                'bloods': user[3],
                'points': (user[3] * BLOOD_POINTS) + (user[2] * FLAG_POINTS)
            }
        )
    return sorted(results, key=lambda k: k['points'], reverse=True)
