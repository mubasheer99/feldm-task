/*
------------------------------------------------------------------------------
File        : Transactions.sql
Project     : FELDM
Author      : MM
Description : definition of table Transactions
------------------------------------------------------------------------------
Changelog :
23.04.2022   MM  : initial definition of  Transactions tables
24.04.2022   MM  : Added column revenue_eur
------------------------------------------------------------------------------
*/

    CREATE TABLE Transactions(
           id               INTEGER PRIMARY KEY AUTOINCREMENT,
           datetime         DATE,
           visitor_id       INTEGER,
           device_type      INTEGER,
           revenue          REAL,
           revenue_eur      REAL,
           tax              REAL,
           FOREIGN KEY(device_type) REFERENCES Devices(id)
    )
