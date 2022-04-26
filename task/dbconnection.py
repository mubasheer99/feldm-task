#  File        : dbconnection.py
#  Project     : FELDM
#  Author      : MM
#  Description : Module for  different Database connections
######################################################################
#  Changelog :
#  23.04.2022   MM  : initial definition of  currencyconverter file
############################################################################
import sqlite3
from sqlite3 import Error
import psycopg2
from configparser import ConfigParser


def create_sqlliteconnection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
        :param db_file: database file location
        :return: Connection object or None
    """
    conn = None

    try:
        print('Connecting to the sqllite database......')
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as error:
        print('Error occured - ', error)

    return conn


def config(section='postgresql', filename='.env'):
    """ configuration to connect to get db connection params
        specified by the db_file
        :param section: section in the .env file
        :param filename: filename to look for connection details
        :return: Connection object or None
    """
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section,
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def create_pgconnection(section):
    """ create a database connection to the PostgreSQL database
        specified by the db_file
        :param section: section in the .env file
        :return: Connection object or None
    """
    conn = None
    try:
        # read connection parameters
        params = config(section)

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn


def connect_with_sqlalchemy(db_url):
    """ create a database connection to the PostgreSQL database
        specified by the db_file
        :param db_url: database file location
        :return: Connection object or None
    """

    connection = None
    try:
        print('Connecting to the sqllite database with alchemy......')
        engine = db.create_engine(db_url)
        connection = engine.connect()
    except sqlite3.Error as error:
        print('Error occured - ', error)

    return connection



