CREATE KEYSPACE lab_hashing 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE lab_hashing;

CREATE TABLE sensor_hashes (
    sensor_id UUID PRIMARY KEY,
    location TEXT,
    data_value FLOAT
);