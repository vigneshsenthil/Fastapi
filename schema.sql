DROP DATABASE IF EXISTS `DB`;
CREATE DATABASE `DB`;
USE `DB`;
CREATE TABLE IF NOT EXISTS `bseindia`(
    Deal_date varchar(100) not null,
    security_code int not null,
    Securite_name varchar(100) not null,
    Client_Name	 varchar(100) not null,
    Deal_Type varchar(100) not null,
    Quantity	int not null,
    Price FLOAT not null)