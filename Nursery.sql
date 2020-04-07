create database nursery;
use nursery;

create table plant (
	id integer not null,
    name varchar(20) not null,
    price decimal(10,2),
    description varchar(50),
    age integer,
    primary key(id),
    unique(name)
);


create table plant_type (
	type_id integer not null,
    type_name varchar(20) not null,
    description varchar(50),
    primary key(type_id),
    unique(type_name)
);


create table store (
	store_id integer not null,
    number_of_lots integer,
    phone_no char(10),
    address varchar(50),
    primary key(store_id)
);

create table customer (
	cust_id integer not null,
    cust_name varchar(20) not null,
    phone_no char(10),
    address varchar(50),
    email_id varchar(20),
    primary key(cust_id)
);


create table orders (
	order_id integer not null,
    store_id integer not null,
    cust_id integer not null,
    order_type varchar(20),
    payment_status varchar(20),
    price decimal(10,2),
    delivery_address varchar(50),
    primary key(order_id),
    unique(order_type),
    foreign key(store_id) references store(store_id),
    foreign key(cust_id) references customer(cust_id)
);


create table order_item (
	order_id integer not null,
    item_id integer not null,
    price decimal(10,2),
    rating decimal(2,1),
    plant_id integer not null,
    primary key(item_id),
    foreign key(order_id) references orders(order_id),
    foreign key(plant_id) references plant(id)
);


create table employee (
	emp_id integer not null,
    emp_name varchar(20) not null,
    store_id integer not null,
    doj date,
    phone_no char(10),
    designation varchar(20),
    supervisor_id integer,
    primary key(emp_id),
    unique(emp_name),
    foreign key(store_id) references store(store_id)
);
    
    
