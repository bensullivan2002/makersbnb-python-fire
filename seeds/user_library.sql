DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT,
    password TEXT,
    is_logged_on BOOLEAN
);

INSERT INTO users (email, password, is_logged_on) VALUES ('example1@hotmail.com', 'Password12345', False);
INSERT INTO users (email, password, is_logged_on) VALUES ('example2@hotmail.com', 'Password12345', False);