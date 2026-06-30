DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS admins;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    gender TEXT,
    age INTEGER,
    telephone TEXT,
    email TEXT UNIQUE,
    address TEXT,
    experience TEXT,
    profile_image TEXT,
    state INTEGER DEFAULT 1
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

INSERT INTO users (
    username,
    password,
    gender,
    age,
    telephone,
    email,
    address,
    experience,
    profile_image,
    state
) VALUES (
    'testuser',
    'test123',
    'Female',
    22,
    '0400000000',
    'testuser@example.com',
    'Perth, WA',
    'Has pet care experience',
    'user1.jpg',
    1
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
