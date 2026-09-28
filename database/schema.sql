-- The tables this project needs.
--
-- Run this against your database once you have a DATABASE_URL, with:
--   cat database/schema.sql | ssh dokku@iscs2.gcsu.edu mysql:import <your-app-name>

CREATE TABLE IF NOT EXISTS albums (
    id                    INT AUTO_INCREMENT PRIMARY KEY,
    title                 VARCHAR(100) NOT NULL,
    release_year          INT NOT NULL,
    record_label          VARCHAR(100),
    copies_sold_millions  DECIMAL(5,1),
    description           TEXT,
    created_at            TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
