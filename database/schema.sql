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
