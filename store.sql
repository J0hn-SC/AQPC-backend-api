create database store;
use store;

create table User(
	id_user integer unique auto_increment,
    given_name varchar(30) not null,
    family_name varchar(30) not null,
    email varchar(30) unique not null,
    primary key(id_user)
);

create table Product(
    id_product integer unique auto_increment,
    naming varchar(30) not null,
    brand varchar(30) not null,
    price float not null,
    details varchar(255) not null,
    primary key (id_product)
);

create table Offering(
    id_offering integer unique auto_increment,
    price float not null,
    primary key (id_offering),
    foreign key (id_offering) references Offering(id_offering)
);