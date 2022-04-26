#  File        : config.py
#  Project     : FELDM
#  Author      : MM
#  Description : contains teh configuration details of the  project
######################################################################
#  Changelog :
#  23.04.2022   MM  : initial definition of  config file
############################################################################

xpath_variable = '//*[@currency]'
curr_to_convert = 'USD'
XML_path = 'eurofxref-hist-90d.xml'
xpath_root_variable = ['gesmes:Envelope', 'Cube']
log_file = 'log.txt'

task1_query = r'''with revenue as
                (select  visitor_id ,max(total_revenue) revenue FROM
                (select visitor_id,sum(revenue) total_revenue from Transactions group by visitor_id order by 2 desc)
                group by visitor_id order by 2 desc)
                select * from revenue
                where revenue >=(select max(revenue) from revenue)'''

task2_query = r'''select t.datetime revenue_date,sum(revenue) revenue from devices d,Transactions t
                where d.id=t.device_type and d.device_name='Mobile Phone'
                group by t.datetime order by 2 desc'''

task3_query = {'devices': 'select id device_id,device_name from devices', 'transaction': 'select * from Transactions'}

task5_query = {'create': 'CREATE TABLE IF NOT EXISTS Devices(id     INTEGER,device_name TEXT,PRIMARY KEY(id))', 'insert': '''INSERT INTO Devices ("id","device_name") VALUES (1,'Desktop'),(2,'Tablet'),(3,'Mo bile Phone'),(4,'Unknown') ON CONFLICT (id) DO NOTHING;''', 'select': 'select * from devices'}
