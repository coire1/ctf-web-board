drop table if exists challenges;
    create table challenges (
    id integer primary key autoincrement,
    name text,
    address text,
    description text,
    flag text
);


drop table if exists points;
    create table points (
    id integer primary key autoincrement,
    username text,
    challenge_id integer,
    created_at timestamp default current_timestamp,
    blood boolean
);
