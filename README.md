# CTF web board
A simple skeleton to make a score board for CTFs.
The board uses [`Flask`](http://flask.pocoo.org/) to provide a simple HTTP API
and [`Vue.js`](https://vuejs.org/) for the web app client and
[`Sqlite`](https://www.sqlite.org/index.html) as database.
There is no authentication - users just insert their username on flag
submitting - and rank is calculated grouping usernames.
A simple `cli` is provided to add challenges and to reset rank.

## Getting started

Install python dependencies:

    pip install sqlite hashlib flask argparse

Create the database:

    sqlite3 db/database.db < db/schema.sql

In `server/models.py` some constants can be changed (optional):

    FLAG_POINTS: points assigned for a captured flag
    BLOOD_POINTS: points assigned for a captured blood

Install npm dependencies:

    cd client
    npm install

Config api host editing `client/.env`, the Vue enviroment file:

    VUE_APP_API_BASE_URL="http://localhost:5000/"

Build web app:

    cd client
    npm run build

Link the client (if link is not already here):

    cd server
    ln -s ../client/dist static

Run the server:

    python server/main.py

Add a challenge:

    python server/cli.py --insert --name bof2 --address "ssh -p2223 bof2@127.0.0.1" --description "Bof2 description" --flag ok`

Reset rank:

    python server/cli.py --reset
