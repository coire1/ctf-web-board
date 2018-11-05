import sqlite3 as sql
import hashlib
import time


DATABASE_PATH = '../db/database.db'

def getChallenges():
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute("SELECT id, name, address, description, base_points, blood_points FROM challenges")
    challenges = cur.fetchall()
    con.close()
    results = []
    for challenge in challenges:
        results.append(
            {
                'id': challenge[0],
                'name': challenge[1],
                'address': challenge[2],
                'description': challenge[3],
                'base_points': challenge[4],
                'blood_points': challenge[5]
            }
        )
    return results


def getChallenge(challenge_id):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "SELECT id, name, address, description, base_points, blood_points FROM challenges WHERE id=?",
        (int(challenge_id),)
    )
    challenge = cur.fetchone()
    con.close()
    return {
        'id': challenge[0],
        'name': challenge[1],
        'address': challenge[2],
        'description': challenge[3],
        'base_points': challenge[4],
        'blood_points': challenge[5]
    }


def checkChallenge(challenge_id, key, username):
    result = False
    blood = False
    exists = False
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "SELECT id, base_points, blood_points FROM challenges WHERE id=? AND flag=?",
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
            blood_points = challenge[2] if blood else 0
            cur.execute(
                "INSERT INTO \
                points(username, challenge_id, created_at, base_points, blood_points, blood) \
                VALUES (?, ?, ?, ?, ?, ?)",
                (
                    str(username),
                    int(challenge_id),
                    time.time(),
                    int(challenge[1]),
                    int(blood_points),
                    blood
                )
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
        (SUM(base_points) + SUM(blood_points)) AS agg_points, \
        SUM(blood) AS agg_bloods \
        FROM points \
        GROUP BY username \
        ORDER BY agg_points DESC, agg_bloods DESC \
    ")
    users = cur.fetchall()
    con.close()
    results = []
    for user in users:
        results.append(
            {
                'id': user[0],
                'username': user[1],
                'points': user[2],
                'bloods': user[3]
            }
        )
    return results


def getChallengeRank(challenge_id):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute("SELECT \
        id, \
        username, \
        (SUM(base_points) + SUM(blood_points)) AS agg_points, \
        SUM(blood) AS agg_bloods \
        FROM points \
        WHERE challenge_id = ? \
        GROUP BY username \
        ORDER BY agg_points DESC, created_at ASC \
    ", (int(challenge_id),))
    users = cur.fetchall()
    con.close()
    results = []
    for user in users:
        results.append(
            {
                'id': user[0],
                'username': user[1],
                'points': user[2],
                'bloods': user[3]
            }
        )
    return results
