import sqlite3 as sql
import hashlib
import argparse

DATABASE_PATH = '../db/database.db'


def insertChallenge(name, address, description, flag, base_points, blood_points):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "SELECT id FROM challenges WHERE name = ?",
        (
            str(name),
        )
    )
    assert (cur.rowcount == 0), "challenge {} already exists".format(name)
    cur.execute(
        "INSERT INTO challenges(name, address, description, flag, base_points, blood_points) \
         VALUES (?, ?, ?, ?, ?, ?)",
        (
            str(name),
            str(address),
            str(description),
            hashlib.md5(flag.encode('utf8')).hexdigest(),
            int(base_points),
            int(blood_points),
        )
    )
    con.commit()

def updateChallenge(name, address, description, flag, base_points, blood_points):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "UPDATE challenges SET address = ?, description = ?, flag = ?, base_points = ?, blood_points = ? \
         WHERE name=?",
        (
            str(address),
            str(description),
            hashlib.md5(flag.encode('utf8')).hexdigest(),
            int(base_points),
            int(blood_points),
            str(name),
        )
    )
    con.commit()

def getChallengeByName(name):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "SELECT address, description, flag, base_points, blood_points FROM challenges\
         WHERE name=?",
        (
            str(name),
        )
    )
    row = cur.fetchone();
    if (row == None):
        raise Exception("challenge {} not found".format(name))
    else:
        return row

def resetRank():
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "DELETE FROM points"
    )
    con.commit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', dest='name', help='The name of the challenge')
    parser.add_argument('--address', dest='address', help='The ssh address of the challenge')
    parser.add_argument('--description', dest='description', help='The description of the challenge')
    parser.add_argument('--flag', dest='flag', help='The flag for the challenge')
    parser.add_argument('--base-points', dest='base_points', help='The points assigned for the challenge')
    parser.add_argument('--blood-points', dest='blood_points', help='The points assigned for the blood')
    parser.add_argument('--insert', action='store_true', default=False,
                    dest='insert',
                    help='Insert a new challenge.')
    parser.add_argument('--update', action='store_true', default=False,
                    dest='update',
                    help='Update the challenge with the given name.')
    parser.add_argument('--reset', action='store_true', default=False,
                    dest='reset',
                    help='Drop the rank.')
    args = parser.parse_args()
    if (args.insert):
        if(args.name and args.address and args.description and args.flag and args.base_points and args.blood_points):
            name = args.name.strip()
            address = args.address.strip()
            description = args.description.strip()
            flag = args.flag.strip()
            base_points = args.base_points.strip()
            blood_points = args.blood_points.strip()
            insertChallenge(name, address, description, flag, base_points, blood_points)
        else:
            print "Please enter --name, --address, --description, --flag, --base-points, --blood-points"
    if (args.update):
        if(args.name):
            (address, description, flag, base_points, blood_points) = getChallengeByName(args.name)
            if(args.address):
                address = args.address.strip()
            if(args.description):
                description = args.description.strip()
            if(args.flag):
                flag = args.flag.strip()
            if(args.base_points):
                base_points = args.base_points.strip()
            if(args.blood_points):
                blood_points = args.blood_points.strip()
            updateChallenge(args.name, address, description, flag, base_points, blood_points)
        else:
            print "Please enter the name of the challenge to update"
    elif (args.reset):
        resetRank()


if __name__ == '__main__':
    main()
