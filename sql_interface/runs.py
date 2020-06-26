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