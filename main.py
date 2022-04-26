#  File        : main.py
#  Project     : FELDM
#  Author      : MM
#  Description : The entry point from where project will run
######################################################################
#  Changelog :
#  23.04.2022   MM  : initial definition of  main file
############################################################################
import os
import logging
from task import config, dbconnection, tasks, currencyconverter
from dotenv import load_dotenv

# logging.basicConfig(filename=config.log_file, encoding='utf-8', level=logging.info)
# load environment file
load_dotenv()

# get the config details from .env and config files
database = os.environ.get('db_url')
database_alchemy = os.environ.get('SQLALCHEMY_DATABASE_URL')
ecb_url = os.environ.get('ecb_url')
path_variable = config.xpath_variable
path_root_variable = config.xpath_root_variable
curr = config.curr_to_convert
xml_path = config.XML_path


def main():

    conversion_rate = currencyconverter.get_latest_conversion(ecb_url, path_variable, curr)
    # print(f'the conversion rate is {conversion_rate}')

    historical_data = currencyconverter.get_historical_conversion(xml_path, path_root_variable, curr)
    # print(historical_data.head())

    # create a sqllite database connection
    conn = dbconnection.create_sqlliteconnection(database)

    # create an instance of Task class
    tasklist = tasks.Tasks(conn)
    print('............starting task1:Visitor with Highest Revenue....................')
    tasklist.task1(config.task1_most_revenue_user)
    print('............completed task1:Visitor with Highest Revenue...................')

    print('............starting task2:Date with Highest Revenue....................')
    tasklist.task2(config.task2_most_revenue_day)
    print('............completed task2:Date with Highest Revenue...................')

    print('............starting task3:Combine devices and transactions....................')
    tasklist.task3(**config.task3_combine_tables)
    print('.........completed task3 check the file combine_data.xlsx in the root......')

    print('............starting task4:Update revenue to EUR....................')
    tasklist.task4_current(conversion_rate)
    print('............completed task4:Update revenue to EUR...................')

    print('...........starting task4 with historical data.........')
    tasklist.task4_historical(historical_data, **config.task3_combine_tables)
    print('............completed task4 with historical data check combine_histdata.xlsx file......')
    # close the DB connection
    conn.close()

    print('..................starting task5:Postgressql connection...............')
    # create a postgress  database connection
    pgdb = dbconnection.create_pgconnection('postgresql')
    # create an instance of Task class
    pgtask = tasks.Tasks(pgdb)
    pgtask.task5(**config.task5_create_insert_table)
    print('..................completed task5:Postgressql connection..............')
    # close the DB connection
    pgdb.close()


if __name__ == "__main__":
    main()









