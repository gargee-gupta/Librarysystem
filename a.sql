drop database test
create database test
use test
drop table if exists library
create table library(book_code int Unique,book_name varchar(50),author varchar(25),publisher varchar(25),price int,stock text, edition varchar(10))
#INSERTING VALUES 
insert into library values(1021,'The Seal of Surya','Amritanshu Pandey','Pirates',175,25,'1st')
insert into library values(2403,'Matilda','Roald Dahl','Penguin',200,30,'3rd')
insert into library values(0082,'Think and grow rich','Napoleon Hill','Penguin',325,10,'5th')
insert into library values(2651,'My Journey','A.P.J. Abdul Kalam','Rupa',190,8,'1st')
insert into library values(3120,'Adventures of Sherlock Holmes','Sir Arthur conan doyle','Maple Press',225,20,'4th')
insert into library values(1026,'The Secret','Rhonda Byrne','Penguin',150,12,'2nd')
insert into library values(1258,'The Alchemist','Paulo Coelho','HarperCollins',200,21,'6th')
insert into library values(2638,'Ace against odds','Sania Mirza','Harpercollins',300,12,'3rd')

