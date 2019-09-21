CREATE USER trivia WITH PASSWORD 'trivia';
CREATE DATABASE opentrivia_prod;
CREATE DATABASE opentrivia_test;
GRANT ALL PRIVILEGES ON DATABASE opentrivia_prod TO trivia;
GRANT ALL PRIVILEGES ON DATABASE opentrivia_test TO trivia;