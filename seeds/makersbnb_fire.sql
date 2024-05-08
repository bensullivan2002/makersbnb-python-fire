DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq CASCADE;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq CASCADE;
DROP TABLE IF EXISTS dates_available CASCADE;
DROP SEQUENCE IF EXISTS dates_available_id_seq CASCADE;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(64),
    password VARCHAR(32),
    first_name text,
    last_name text,
    phone_number VARCHAR(30)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    price_per_night int,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    start_date date,
    end_date date,
    user_id int,
    space_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade
);

CREATE SEQUENCE IF NOT EXISTS dates_available_id_seq;
CREATE TABLE dates_available (
    id SERIAL PRIMARY KEY,
    start_date date,
    end_date date,
    space_id int,
    constraint fk_space foreign key(space_id)
        references spaces(id)
        on delete cascade
);

INSERT INTO users (email, password, first_name, last_name, phone_number) VALUES ('ben@gmail.com', 'Password123!', 'Ben', 'Sullivan', '07223487567');
INSERT INTO users (email, password, first_name, last_name, phone_number) VALUES ('angelica@gmail.com', 'Password567!', 'Angelica', 'Gottlieb', '07895687907');

INSERT INTO spaces (name, description, price_per_night, user_id) VALUES ('Treehouse', '1 bed unique stay', 150, 1);
INSERT INTO spaces (name, description, price_per_night, user_id) VALUES ('Ocean Apartment', 'Luxury stay by the sea', 200, 2);

INSERT INTO bookings (start_date, end_date, user_id, space_id) VALUES ('2024-05-12', '2024-05-19', 1, 2);
INSERT INTO bookings (start_date, end_date, user_id, space_id) VALUES ('2024-07-13', '2024-07-28', 2, 1);

INSERT INTO dates_available (start_date, end_date, space_id) VALUES ('2024-01-01', '2025-01-01', 1);
INSERT INTO dates_available (start_date, end_date, space_id) VALUES ('2024-01-01', '2025-01-01', 2);