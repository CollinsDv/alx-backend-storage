-- A script that creates a table users
-- Attributes: (id, email, name)
-- shouldn't fail if script exists and executable on any database
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
