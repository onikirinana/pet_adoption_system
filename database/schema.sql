DROP TABLE IF EXISTS answers;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS adoption_records;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS blogs;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS admins;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    sex TEXT,
    age INTEGER,
    telephone TEXT,
    email TEXT UNIQUE,
    address TEXT,
    pic TEXT,
    state INTEGER DEFAULT 0 CHECK (state IN (0, 1))
);

CREATE TABLE admins (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_name TEXT NOT NULL UNIQUE,
    admin_password TEXT NOT NULL,
    real_name TEXT,
    telephone TEXT,
    email TEXT UNIQUE,
    birthday TEXT,
    gender TEXT,
    profile_image TEXT,
    remark TEXT
);

CREATE TABLE adoption_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    pet_id INTEGER NOT NULL,
    adopt_time TEXT,
    state INTEGER DEFAULT 0
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    admin_id INTEGER,
    pet_id INTEGER,
    comment_time TEXT DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL
);

CREATE TABLE answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    reply_id INTEGER,
    comment_id INTEGER NOT NULL,
    answer_time TEXT DEFAULT CURRENT_TIMESTAMP,
    content TEXT NOT NULL
);

CREATE TABLE applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    telephone TEXT,
    message TEXT,
    apply_time TEXT DEFAULT CURRENT_TIMESTAMP,
    state INTEGER DEFAULT 0
);

CREATE TABLE blogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action_time TEXT DEFAULT CURRENT_TIMESTAMP,
    address TEXT,
    people TEXT,
    event TEXT,
    title TEXT NOT NULL
);

CREATE TABLE pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pet_name TEXT NOT NULL,
    pet_type TEXT NOT NULL,
    sex TEXT,
    birthday TEXT,
    pic TEXT,
    state INTEGER DEFAULT 0 CHECK (state IN (0, 1, 2)),
    remark TEXT
);

INSERT INTO users (
    username,
    password,
    sex,
    age,
    telephone,
    email,
    address,
    pic,
    state
) VALUES (
    'testuser',
    'test123',
    'Female',
    22,
    '0400000000',
    'testuser@example.com',
    'Perth, WA',
    'user1.jpg',
    0
);

INSERT INTO admins (
    admin_name,
    admin_password,
    real_name,
    telephone,
    email,
    birthday,
    gender,
    profile_image,
    remark
) VALUES (
    'admin',
    'admin123',
    'System Administrator',
    '0499999999',
    'admin@example.com',
    '1995-01-01',
    'Female',
    'admin1.jpg',
    'Main system administrator'
);
