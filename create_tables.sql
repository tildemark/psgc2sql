-- Provinces Table
CREATE TABLE Provinces (
    province_id INT PRIMARY KEY AUTO_INCREMENT,
    province_name VARCHAR(255) NOT NULL,
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES Countries(country_id)
);

-- Cities Table
CREATE TABLE Cities (
    city_id INT PRIMARY KEY AUTO_INCREMENT,
    city_name VARCHAR(255) NOT NULL,
    province_id INT,
    FOREIGN KEY (province_id) REFERENCES Provinces(province_id)
);

-- Sub-Cities/Municipalities Table
CREATE TABLE SubCities (
    sub_city_id INT PRIMARY KEY AUTO_INCREMENT,
    sub_city_name VARCHAR(255),
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES Cities(city_id)
);

-- Barangays Table
CREATE TABLE Barangays (
    barangay_id INT PRIMARY KEY AUTO_INCREMENT,
    barangay_name VARCHAR(255) NOT NULL,
    sub_city_id INT,
    city_id INT,
    FOREIGN KEY (sub_city_id) REFERENCES SubCities(sub_city_id),
    FOREIGN KEY (city_id) REFERENCES Cities(city_id)
);

-- Zip Codes Table
CREATE TABLE ZipCodes (
    zip_code VARCHAR(10) PRIMARY KEY,
    city_id INT,
    province_id INT,
    FOREIGN KEY (city_id) REFERENCES Cities(city_id),
    FOREIGN KEY (province_id) REFERENCES Provinces(province_id)
);