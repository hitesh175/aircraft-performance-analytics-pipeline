-- Create Database
CREATE DATABASE aircraft_db;
USE aircraft_db;

-- Create Main Aircraft Table
CREATE TABLE aircraft_data (
    company VARCHAR(100),
    engine_type VARCHAR(100),
    shp FLOAT,
    auw FLOAT,
    vcruise FLOAT,
    vmax FLOAT,
    roc FLOAT,
    range_value FLOAT,
    aircraft_type VARCHAR(50)
);

-- Create Database User
CREATE USER 'aircraft_user'@'localhost' IDENTIFIED BY 'aircraft123';

-- Grant Access to the Database
GRANT ALL PRIVILEGES ON aircraft_db.* TO 'aircraft_user'@'localhost';
FLUSH PRIVILEGES;

-- Insert Sample Record
INSERT INTO aircraft_data
(company, engine_type, shp, auw, vcruise, vmax, roc, range_value, aircraft_type)
VALUES
('Test Aircraft','Jet',5000,15000,250,300,2000,2000,'Airplane');

-- View Data
SELECT * FROM aircraft_data;