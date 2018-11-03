import sqlite3 as sql
import hashlib
import argparse

DATABASE_PATH = '../db/database.db'


def insertChallenge(name, address, description, flag):
    con = sql.connect(DATABASE_PATH)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO challenges(name, address, description, flag) \
         VALUES (?, ?, ?, ?)",
        (
            str(name),
            str(address),
            str(description),
            hashlib.md5(flag.encode('utf8')).hexdigest(),
        )
    )
    con.commit()


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
    parser.add_argument('--flag', dest='flag', help='The flag for the challenge in MD')
    parser.add_argument('--insert', action='store_true', default=False,
                    dest='insert',
                    help='Insert a new challenge.')
    parser.add_argument('--reset', action='store_true', default=False,
                    dest='reset',
                    help='Drop the standing.')
    args = parser.parse_args()
    if (args.insert):
        if(args.name and args.address and args.description and args.flag):
            name = args.name.strip()
            address = args.address.strip()
            description = args.description.strip()
            flag = args.flag.strip()
            insertChallenge(name, address, description, flag)
        else:
            print "Please enter --name, --address, --description, --flag"
    elif (args.reset):
        resetRank()


if __name__ == '__main__':
    main()
