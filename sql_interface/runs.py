import sqlite3
from sql_interface.interface import Table
import datetime

class Runs(Table):
    """
    TODO(Oliver) add in specific functions here.


    """
    table_name = "runs"

    def run_data_check(self):
        """

        :return: exits program if
        """
        assert(type(self.write_data[0]) == type(datetime.datetime.now().date()))
        assert(type(self.write_data[1]) == str)
        assert(type(self.write_data[2]) == int)
        assert(type(self.write_data[3]) == str)
        assert(type(self.write_data[4]) == float)


    def write_to_runs(self):
        """
        :return: no return, just inserts into database
        """
        cursor = self.connection.cursor()

        sqlite_insert_str = \
            """INSERT INTO %s values (?, ?, ?, ?, ?)""" % self.table_name

        cursor.execute(sqlite_insert_str, self.write_data)

        self.connection.commit()