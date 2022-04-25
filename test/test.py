import unittest
import os
from task import config, dbconnection, tasks, currencyconverter
from dotenv import load_dotenv

load_dotenv()

database = os.environ.get('db_url')
ecb_url = os.environ.get('ecb_url')
path_variable = config.xpath_variable
path_root_variable = config.xpath_root_variable
curr = config.curr_to_convert
xml_path = config.XML_path


class TestTask(unittest.TestCase):

    def test_task1(self):

        # create a database connection
        conn = dbconnection.create_sqlliteconnection(database)

        tasklist = tasks.Tasks(conn)
        result = tasklist.task1(config.task1_query)
        print(result)

        self.assertEqual(result, 5733.5124)
        conn.close()

    def test_task2(self):

        # create a database connection
        conn = dbconnection.create_sqlliteconnection(database)

        tasklist = tasks.Tasks(conn)
        result = tasklist.task2(config.task2_query)
        print(result)

        self.assertEqual(result, '2019-09-20 00:00:00')
        conn.close()


if __name__ == "__main__":
    m = TestTask()
    m.test_task1()
    m.test_task2()



