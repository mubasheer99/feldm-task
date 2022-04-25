/* ------------------------------------------------------------------------------
File        : build.sql
Project     : FELDM
Author      : MM
Description : schema build/setup
------------------------------------------------------------------------------
Changelog :
23.04.2022   MM  : initial definition of  build
------------------------------------------------------------------------------
*/

--Tables
@./Tables/Devices.sql
@./Tables/Transactions.sql
@loaddata.sql

