/*
------------------------------------------------------------------------------
File        : Transactions-0001.sql
Project     : FELDM
Author      : MM
Description : definition of table Transactions
------------------------------------------------------------------------------
Changelog :
23.04.2022   MM  : initial definition of  Transactions tables
------------------------------------------------------------------------------
*/

CREATE TABLE Transactions(
       id               INTEGER PRIMARY KEY AUTOINCREMENT,
       datetime         INTEGER,
       visitor_id       INTEGER,
       device_type      INTEGER,
       revenue          REAL,
       tax              REAL,
       FOREIGN KEY(device_type) REFERENCES Devices(id)
)
