/*
------------------------------------------------------------------------------
File        : Transactions-0002.sql
Project     : FELDM
Author      : MM
Description : Modification of table Transactions
------------------------------------------------------------------------------
Changelog :
24.04.2022   MM  : Added column revenue_eur
------------------------------------------------------------------------------
*/
alter table Transactions add revenue_eur REAL;
