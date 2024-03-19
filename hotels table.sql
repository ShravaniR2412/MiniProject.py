create database travel_buddy;
use travel_buddy;
select * from login

insert into login
values('mahvish', 'mahvish');

select * from city

create table city(
city_name VARCHAR(255) PRIMARY KEY
);

insert into city
values('Mumbai'),('Delhi'), ('Goa');

CREATE TABLE hotel (
    hotel_id SERIAL PRIMARY KEY,
    city_name VARCHAR(255) REFERENCES city(city_name),
    hotel_name VARCHAR(255) NOT NULL,
    cost DECIMAL(10, 2),
    rating DECIMAL(3, 1),
    description TEXT,
    image_path VARCHAR(255)
);

INSERT INTO hotel (city_name, hotel_name, description, rating, cost, image_path)
VALUES
    ('Mumbai', 'Trident Nariman Point', 'Hotel in South Mumbai, Mumbai. It is located in Mumbai, overlooking the beautiful Arabian Sea from Marine Drive', 5, 12000, 'assets/img.png'),
    ('Mumbai', 'Trident Bandra Kurla', 'It provides an outdoor swimming pool and full spa services. Concierge services and room service are available 24 hours. On-site parking is free.', 4.5, 9000, 'assets/img.png'),
    ('Mumbai', 'Hotel Imperial', '1.1 km from beach. Ideally set in Mumbai, Hotel Imperial features air-conditioned rooms with free WiFi, private parking and room service.', 3.4, 4000, 'assets/img.png'),
    ('Mumbai', 'BKC Annex', 'Hotel BKC ANNEX is located 8.6 km from Powai Lake, 9.4 km from Prithvi Theatre and 9.4 km from Dadar Railway Station', 3.6, 6000, 'assets/img.png'),
    ('Mumbai', 'Taj Sanatcruz', 'Offering breath-taking views of the runway from the largest rooms in the city', 4.2, 9000, 'assets/img.png'),
    ('Mumbai', 'JW Marriot', 'Located 400m from Airport and offering an outdoor swimming pool, fitness centre and a spa wellness centre', 4.7, 10000, 'assets/img.png');

select * from hotel

