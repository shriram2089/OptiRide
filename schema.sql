CREATE TABLE drivers (
    driver_id SERIAL PRIMARY KEY,
    location GEOMETRY(POINT, 4326),
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE rides (
    ride_id SERIAL PRIMARY KEY,
    rider_id INTEGER NOT NULL,
    driver_id INTEGER NOT NULL,
    location GEOMETRY(POINT, 4326),
    destination GEOMETRY(POINT, 4326),
    status VARCHAR(50) DEFAULT 'ongoing',
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id)
);
