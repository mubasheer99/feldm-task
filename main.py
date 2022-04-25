# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from task import config, dbconnection, tasks, currencyconverter
from dotenv import load_dotenv
import test

load_dotenv()

database = os.environ.get('db_url')
database_alchemy = os.environ.get('SQLALCHEMY_DATABASE_URL')
ecb_url = os.environ.get('ecb_url')
path_variable = config.xpath_variable
path_root_variable = config.xpath_root_variable
curr = config.curr_to_convert
xml_path = config.XML_path



# database = config.dbname

def main():

    conversion_rate = currencyconverter.get_latest_conversion(ecb_url, path_variable, curr)
    # print(f'the conversion rate is {conversion_rate}')

    historical_data = currencyconverter.get_historical_conversion(xml_path, path_root_variable, curr)
    # print(historical_data.head())

    # create a database connection
    conn = dbconnection.create_sqlliteconnection(database)

    tasklist = tasks.Tasks(conn)
    print('............starting task1....................')
    tasklist.task1(config.task1_query)
    print('............completed task1...................')

    print('............starting task2....................')
    tasklist.task2(config.task2_query)
    print('............completed task2...................')

    print('............starting task3....................')
    tasklist.task3(**config.task3_query)
    print('.........completed task3 check the file combine_data.xlsx in the root......')

    print('............starting task4....................')
    tasklist.task4_current(conversion_rate)
    print('............completed task4...................')

    print('...........starting task4 with historical data.........')
    tasklist.task4_historical(historical_data, **config.task3_query)
    print('............completed task4 with historical data check combine_histdata.xlsx file......')
    conn.close()

    print('..................starting task5...............')
    pgdb = dbconnection.create_pgconnection('postgresql')
    pgtask = tasks.Tasks(pgdb)
    pgtask.task5(**config.task5_query)
    print('..................completed task5..............')
    pgdb.close()

    te


if __name__ == "__main__":
    main()









