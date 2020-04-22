drop database if exists nursery;
create database nursery;
use nursery;

create table store (
   store_id integer not null AUTO_INCREMENT,
   number_of_lots integer,
   phone_no char(10),
   address varchar(50),
   primary key(store_id)
);

create table lot(
   store_id integer NOT NULL,
   lot_id integer NOT NULL,
   primary key(store_id, lot_id),
   foreign key(store_id) references store(store_id) ON DELETE CASCADE
);

create table plant_type (
   type_id integer not null AUTO_INCREMENT,
   type_name varchar(20) not null,
   description varchar(200),
   primary key(type_id),
   unique(type_name)
);

create table plant (
   plant_id integer not null AUTO_INCREMENT,
   name varchar(20) not null,
   price decimal(10,2),
   description varchar(200),
   age integer,
   p_type_id integer,
   primary key(plant_id),
   unique(name),
   foreign key(p_type_id) references plant_type(type_id) ON DELETE SET NULL
);

create table plant_locator (
   p_locator_id integer not null AUTO_INCREMENT,
   plant_id integer not null,
   store_id integer not null,
   lot_id integer not null,
   primary key(p_locator_id),
   foreign key(plant_id) references plant(plant_id) ON DELETE CASCADE,
   foreign key(store_id, lot_id) references lot(store_id, lot_id) ON DELETE CASCADE
);

create table customer (
   cust_id integer not null AUTO_INCREMENT,
   cust_name varchar(20) not null,
   cust_username varchar(50) not null,
   cust_password varchar(50) not null,
   phone_no char(10),
   address varchar(70),
   email_id varchar(35),
   primary key(cust_id),
   unique(cust_username)
);

create table orders (
   order_id integer not null AUTO_INCREMENT,
   store_id integer,
   cust_id integer not null,
   order_date date,
   order_type varchar(20),
   order_status varchar(20),
   payment_status varchar(20),
   price decimal(10,2),
   expected_delivery_date date,
   delivered_on date,
   delivery_address varchar(70),
   primary key(order_id),
   foreign key(store_id) references store(store_id) ON DELETE set null,
   foreign key(cust_id) references customer(cust_id) ON DELETE CASCADE
);

create table order_item (
   item_id integer not null AUTO_INCREMENT,
   order_id integer not null,
   plant_id integer,
   quantity integer,
   price decimal(10,2),
   rating decimal(2,1),
   primary key(item_id),
   foreign key(order_id) references orders(order_id) ON DELETE CASCADE,
   foreign key(plant_id) references plant(plant_id) ON DELETE set null
);

create table employee (
   emp_id integer not null AUTO_INCREMENT,
   emp_name varchar(20) not null,
   emp_username varchar(50) not null,
   emp_password varchar(50) not null,
   store_id integer not null,
   doj date,
   phone_no char(10),
   designation varchar(20),
   supervisor_id integer,
   primary key(emp_id),
   unique(emp_name),
   unique(emp_username),
   foreign key(store_id) references store(store_id) ON DELETE CASCADE
);
