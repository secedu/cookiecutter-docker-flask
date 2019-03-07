DROP DATABASE IF EXISTS {{cookiecutter.database_name}};
CREATE DATABASE {{cookiecutter.database_name}};

\c {{cookiecutter.database_name}}

DROP USER IF EXISTS {{cookiecutter.database_user}};

CREATE USER {{cookiecutter.database_user}} WITH ENCRYPTED PASSWORD '{{cookiecutter.database_pass}}';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO {{cookiecutter.database_user}};
