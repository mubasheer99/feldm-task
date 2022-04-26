#  File        : task.py
#  Project     : FELDM
#  Author      : MM
#  Description : Core module of the project where all task are performed
######################################################################
#  Changelog :
#  23.04.2022   MM  : initial definition of  task file
############################################################################
import pandas as pd
import sqlite3
import datetime
from sqlite3 import Error
import psycopg2


class Tasks:
    def __init__(self, conn):
        self.conn = conn

    def task1(self, query):
        """
        This function get the visitor with most revenue .Here we query the db to get the max revenue
        :param query: query to get the visitor with max revenue
        :return: returns the visitor with most revenue
        """
        cur = self.conn.cursor()
        cur.execute(query)

        rows = cur.fetchone()
        print('The visitor with most revenue is', rows[0], 'and the revenue created was ', rows[1], 'EUR')
        return round(rows[1], 4)

    def task2(self, query):
        """
        This function get the date  with most revenue by mobile device used mix of query and pandas
        :param query: query to get the revenue by dates
        :return: returns the date with most revenue by mobile device
        """

        df = pd.read_sql(query, self.conn,  parse_dates={"datetime": {"format": "%d/%m/%y"}})
        max_revenue = df['revenue'].max()
        result = df[df['revenue'] == max_revenue]
        blankindex = [''] * len(result)
        result.index = blankindex
        print(f"The maximum revenue by mobile device happened on {result['revenue_date'].to_string(header=False).strip()} and the revenue was {result['revenue'].to_string(header=False).strip()}")
        return result['revenue_date'].to_string(header=False).strip()

    def task3(self, **query):
        """
        This function combines the contents of Devices and Transactions table
        and store it as a single flat file including the column names
        :param query: query passed as dictionary
        :return: returns created flat file and store it on the root directory
        """

        devices = pd.read_sql(query['devices'], self.conn)
        transactions = pd.read_sql(query['transaction'], self.conn)

        combined_file = devices.merge(transactions, how='inner', left_on='device_id', right_on='device_type')
        colseq = ['device_id', 'device_name', 'id', 'datetime', 'visitor_id', 'device_type', 'revenue', 'tax']
        combined_file.to_csv('combine_data.csv', columns=colseq, index=False)
        combined_file.to_excel('combine_data.xlsx', columns=colseq, encoding='utf-8', index=False)

    def task4_current(self, conversion_rate):
        """
        This function update revenue to EUR using the conversion current rate from ECB
        :param conversion_rate:current conversion rate to USD
        :return: updated transaction table
        """

        try:
            sql = '''UPDATE transactions
                        SET revenue = revenue * ?'''
            param = (conversion_rate,)
            cur = self.conn.cursor()
            cur.execute(sql, param)
            self.conn.commit()
            print('revenue updated to EUR - ')
        except sqlite3.Error as error:
            print('Error occurred - ', error)

    def task4_historical(self, historical_data,**query):

        """
        This is an optional as requirement already satisfied in above function task4_current
        This function update revenue to EUR using the conversion current rate from ECB
        :param historical_data:dataframe containing the historical conversion
        :param query:query passed as dictionary
        :return: updated file with currency updated to EUR
        """

        try:
            sql = '''UPDATE transactions
                        SET revenue = revenue * ?'''
            transactions = pd.read_sql(query['transaction'], self.conn)
            transactions['datetime'] = pd.to_datetime(transactions['datetime'], format="%Y-%m-%d")
            combined_file = transactions.merge(historical_data, how='inner', left_on='datetime', right_on='date')

            combined_file['rate'] = combined_file['rate'].astype(float)
            combined_file['revenue_eur'] = combined_file['revenue'] * round(1/combined_file['rate'], 4)
            combined_file.to_excel('combine_histdata.xlsx',  encoding='utf-8', index=False)
        except sqlite3.Error as error:
            print('Error occurred - ', error)

    def task5(self, **query):
        """
        This function   exemplarily uses PostgreSQL.
        :param query:query passed as dictionary
        :return: rows from the database table
        """
        try:

            cur = self.conn.cursor()

            print('checking PostgreSQL database version:')
            cur.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            print(db_version)
            print('create table if not exist')
            cur.execute(query['create'])
            print('........table created.........')
            print('insert data  if not exist')
            cur.execute(query['insert'])
            print('......data inserted.......')
            self.conn.commit()
            print('fetch  data  from postgress database')
            cur.execute(query['select'])

            rows = cur.fetchall()
            print('..........data fetched as follows...........')
            for row in rows:
                print(row)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)






