USE lab4;

INSERT INTO shop (city, street, house_number)
VALUES
	('Kyiv', 'Khreshchatyk', 1),
	('Lviv', 'Shevchenko', 10),
	('Odessa', 'Deribasivska', 20),
	('Dnipro', 'Centralna', 15),
	('Kharkiv', 'Sumska', 25),
	('Vinnytsia', 'Soborna', 30),
	('Chernihiv', 'Peremohy', 5),
	('Uzhhorod', 'Korzo', 8),
	('Rivne', 'Independence', 3),
	('Zhytomyr', 'Mikhaylivska', 18);

INSERT INTO product_category (name)
VALUES
	('Dairy'),
	('Fruits'),
	('Vegetables'),
	('Beverages'),
	('Snacks'),
	('Meat'),
	('Bakery'),
	('Frozen Food'),
	('Seafood'),
	('Cereals');

INSERT INTO employee_position (name)
VALUES
	('Manager'),
	('Cashier'),
	('Delivery Person'),
	('Stock Worker'),
	('Security'),
	('Administrator'),
	('Cleaner'),
	('Marketing Specialist'),
	('Sales Consultant'),
	('HR Specialist');

INSERT INTO manufacturing_company (name, city, street, house_number)
VALUES
	('Roshen', 'Kyiv', 'Leiptsyzka', 1),
	('Coca-Cola Beverages Ukraine', 'Kyiv', 'Vyzvolyteliv', 2),
	('Danone', 'Lviv', 'Hrushevskoho', 15),
	('Nestle', 'Kharkiv', 'Poltavskyi Shlyakh', 40),
	('MHP', 'Cherkasy', 'Pryvokzalna', 22),
	('Carlsberg Ukraine', 'Lviv', 'Stryyska', 39),
	('PepsiCo Ukraine', 'Kyiv', 'Stepana Bandery', 11),
	('AB InBev Efes', 'Dnipro', 'Zavodska', 15),
	('Nestle', 'Vinnytsia', 'Soborna', 30),
	('Philip Morris Ukraine', 'Kharkiv', 'Akademika Pavlova', 5);

INSERT INTO delivery_type (name)
VALUES
	('Standard'),
	('Express');

INSERT INTO client (name, surname, phone_number, email)
VALUES
	('Ivan', 'Ivanov', '+380501234567', 'ivanov@gmail.com'),
	('Petro', 'Petrenko', '+380671234567', 'petrenko@gmail.com'),
	('Oksana', 'Shevchenko', '+380931234567', 'oksana@gmail.com'),
	('Olha', 'Kovalenko', '+380681234567', 'olha@gmail.com'),
	('Serhii', 'Bondar', '+380991234567', 'serhii@gmail.com'),
	('Dmytro', 'Melnyk', '+380951234567', 'dmytro@gmail.com'),
	('Andrii', 'Tkachuk', '+380661234567', 'andrii@gmail.com'),
	('Kateryna', 'Polishchuk', '+380731234567', 'kateryna@gmail.com'),
	('Svitlana', 'Kruts', '+380681234568', 'svitlana@gmail.com'),
	('Oleh', 'Kharchenko', '+380501234568', 'oleh@gmail.com');

INSERT INTO employee (name, surname, phone_number, position_id, shop_id)
VALUES
	('Oleh', 'Koval', '+380501234569', 1, 1),
	('Inna', 'Petrova', '+380671234568', 2, 2),
	('Taras', 'Zhuk', '+380931234569', 3, 3),
	('Mykola', 'Smirnov', '+380681234569', 4, 4),
	('Iryna', 'Lytvyn', '+380991234568', 5, 5),
	('Bogdan', 'Zinchenko', '+380951234568', 6, 6),
	('Yana', 'Kruk', '+380661234568', 7, 7),
	('Anatolii', 'Hrytsenko', '+380731234569', 8, 8),
	('Larysa', 'Chorna', '+380681234569', 9, 9),
	('Nazar', 'Horbach', '+380501234570', 10, 10);

INSERT INTO product (name, price_UAH, description, shelf_time_WEEKS, product_category_id, manufacturing_company_id)
VALUES
	('Roshen Chocolate Bar', 45, 'Dark chocolate bar 100g', 52, 5, 1),
	('Coca-Cola 1L', 20, 'Carbonated soft drink 1L', 12, 4, 2),
	('Danone Yogurt', 25, 'Natural yogurt 400g', 4, 1, 3),
	('Nestle Nescafe Coffee', 150, 'Instant coffee 100g', 104, 4, 4),
	('MHP Chicken Breast', 120, 'Fresh chicken breast 1kg', 1, 6, 5),
	('Carlsberg Beer 0.5L', 30, 'Alcoholic beverage', 24, 4, 6),
	('Lays Chips', 35, 'Potato chips 100g', 20, 5, 7),
	('Pepsi 1L', 22, 'Carbonated soft drink 1L', 12, 4, 8),
	('AB InBev Efes Beer 0.5L', 30, 'Alcoholic beverage', 24, 4, 9),
	('Oreo Cookies', 40, 'Chocolate sandwich cookies 150g', 52, 5, 1);

INSERT INTO shop_product_receiving (product_id, shop_id, date)
VALUES
	(1, 1, '2023-10-01'),
	(2, 1, '2023-10-02'),
	(3, 2, '2023-10-03'),
	(4, 2, '2023-10-04'),
	(5, 3, '2023-10-05'),
	(6, 3, '2023-10-06'),
	(7, 4, '2023-10-07'),
	(8, 4, '2023-10-08'),
	(9, 5, '2023-10-09'),
	(10, 5, '2023-10-10');

INSERT INTO client_product_delivery (client_id, product_id, delivery_type_id, shop_id, city, street, house_number, date)
VALUES
	(4, 10, 1, 1, 'Kyiv', 'Khreshchatyk', 1, '2023-10-11'),
	(3, 9, 2, 2, 'Lviv', 'Shevchenko', 10, '2023-10-12'),
	(3, 8, 1, 3, 'Odessa', 'Deribasivska', 20, '2023-10-13'),
	(1, 7, 2, 4, 'Dnipro', 'Centralna', 15, '2023-10-14'),
	(1, 6, 1, 5, 'Kharkiv', 'Sumska', 25, '2023-10-15'),
	(8, 5, 2, 6, 'Vinnytsia', 'Soborna', 30, '2023-10-16'),
	(3, 4, 1, 7, 'Chernihiv', 'Peremohy', 5, '2023-10-17'),
	(7, 3, 2, 8, 'Uzhhorod', 'Korzo', 8, '2023-10-18'),
	(3, 2, 1, 9, 'Rivne', 'Independence', 3, '2023-10-19'),
	(2, 1, 2, 10, 'Zhytomyr', 'Mikhaylivska', 18, '2023-10-20');

drop procedure if exists get_employee_after_employee_position;
drop procedure if exists get_employee_after_shop;
drop procedure if exists get_product_after_category;
drop procedure if exists get_product_after_manufacturing_company;
drop procedure if exists get_shop_product_receiving_after_shop;
drop procedure if exists get_shop_product_receiving_after_product;
drop procedure if exists get_client_product_delivery_after_client;
drop procedure if exists get_client_product_delivery_after_product;
drop procedure if exists get_client_product_delivery_after_shop;
drop procedure if exists get_client_product_delivery_after_delivery_type;

delimiter ///
create procedure get_employee_after_employee_position(in position_id int)
begin
select e.id, e.name, e.surname, e.phone_number, e.shop_id, p.name as position_name
from employee e join employee_position p on e.position_id = p.id
where e.position_id = position_id;
end ///

create procedure get_employee_after_shop(in shop_id int)
begin
select e.id, e.name, e.surname, e.phone_number, s.id as shop_id, s.city, s.street, s.house_number
from employee e join shop s on e.shop_id = s.id
where e.shop_id = shop_id;
end ///

create procedure get_product_after_category(in category_id int)
begin
select p.id, p.name, p.price_UAH, p.description, p.shelf_time_WEEKS, p.manufacturing_company_id, c.name as category_name
from product p join product_category c on p.product_category_id = c.id
where p.product_category_id = category_id;
end ///

create procedure get_product_after_manufacturing_company(in manufacturing_company_id int)
begin
select p.id, p.name, p.price_UAH, p.description, p.shelf_time_WEEKS, p.product_category_id, m.name as manufacturing_company
from product p join manufacturing_company m on p.manufacturing_company_id = m.id
where p.manufacturing_company_id = manufacturing_company_id;
end ///

create procedure get_shop_product_receiving_after_shop(in shop_id int)
begin
select spr.id, spr.product_id, spr.date, s.id as shop_id, s.city, s.street, s.house_number
from shop_product_receiving spr join shop s on spr.shop_id = s.id
where spr.shop_id = shop_id;
end ///

create procedure get_shop_product_receiving_after_product(in product_id int)
begin
select spr.id, spr.shop_id, spr.date, p.name as product_name
from shop_product_receiving spr join product p on spr.product_id = p.id
where spr.product_id = product_id;
end ///

create procedure get_client_product_delivery_after_client(in client_id int)
begin
select cpd.id, cpd.product_id, cpd.delivery_type_id, cpd.shop_id, cpd.city, cpd.street, cpd.house_number, cpd.date,
c.name as client_name, c.surname as client_surname
from client_product_delivery cpd join client c on cpd.client_id = c.id
where cpd.client_id = client_id;
end ///

create procedure get_client_product_delivery_after_product(in product_id int)
begin
select cpd.id, cpd.client_id, cpd.delivery_type_id, cpd.shop_id, cpd.city, cpd.street, cpd.house_number, cpd.date,
p.name as product_name
from client_product_delivery cpd join product p on cpd.product_id = p.id
where cpd.product_id = product_id;
end ///

create procedure get_client_product_delivery_after_shop(in shop_id int)
begin
select cpd.id, cpd.client_id, cpd.delivery_type_id, cpd.product_id, cpd.city, cpd.street, cpd.house_number, cpd.date,
s.id as shop_id, s.city as shop_city, s.street as shop_street, s.house_number as shop_house_number
from client_product_delivery cpd join shop s on cpd.shop_id = s.id
where cpd.shop_id = shop_id;
end ///

create procedure get_client_product_delivery_after_delivery_type(in delivery_type_id int)
begin
select cpd.id, cpd.client_id, cpd.shop_id, cpd.product_id, cpd.city, cpd.street, cpd.house_number, cpd.date,
d.name as delivery_type_name
from client_product_delivery cpd join delivery_type d on cpd.delivery_type_id = d.id
where cpd.delivery_type_id = delivery_type_id;
end ///
delimiter ;