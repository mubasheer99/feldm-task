import pandas as pd
import sqlite3
import datetime
from sqlite3 import Error


class Tasks:
    def __init__(self, conn):
        self.conn = conn

    def task1(self, query):
        """ This function predicts the most likely symbol that will follow the provided symbol. """
        cur = self.conn.cursor()
        cur.execute(query)

        rows = cur.fetchone()
        print('The visitor with most revenue is', rows[0], 'and the revenue created was ', rows[1], 'EUR')
        return round(rows[1], 4)

    def task2(self, query):

        df = pd.read_sql(query, self.conn,  parse_dates={"datetime": {"format": "%d/%m/%y"}})
        max_revenue = df['revenue'].max()
        result = df[df['revenue'] == max_revenue]
        blankindex = [''] * len(result)
        result.index = blankindex
        print(f"The maximum revenue by mobile device happened on {result['revenue_date'].to_string(header=False).strip()} and the revenue was {result['revenue'].to_string(header=False).strip()}")
        return result['revenue_date'].to_string(header=False).strip()

    def task3(self, **query):

        devices = pd.read_sql(query['devices'], self.conn)
        transactions = pd.read_sql(query['transaction'], self.conn)

        combined_file = devices.merge(transactions, how='inner', left_on='device_id', right_on='device_type')
        colseq = ['device_id', 'device_name', 'id', 'datetime', 'visitor_id', 'device_type', 'revenue', 'tax']
        combined_file.to_csv('combine_data.csv', columns=colseq, index=False)
        combined_file.to_excel('combine_data.xlsx', columns=colseq, encoding='utf-8', index=False)

    def task4_current(self, conversion_rate):

        """
        update priority, begin_date, and end date of a task
        :param conversion_rate:
        :param task:
        :return: project id
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
        update priority, begin_date, and end date of a task
        :param conversion_rate:
        :param task:
        :return: project id
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
        """ This function predicts the most likely symbol that will follow the provided symbol. """
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






