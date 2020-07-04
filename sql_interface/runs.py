from sql_interface.interface import Table
import datetime

class Runs(Table):
    """
    TODO(Oliver) add in specific functions here.


    """
    def __init__(self, param):
        super().__init__(param)
        self.table_name = "runs"

    def run_data_check(self, write_data) -> bool:
        """

        :return: throws error if wrong data types
        """
        if \
        type(write_data[0]) != datetime.date or \
        type(write_data[1]) != float or \
        type(write_data[2]) != int or \
        type(write_data[3]) != str or \
        type(write_data[4]) != float:


            print(type(write_data[0]), datetime.date)
            print(type(write_data[1]), float)
            print(type(write_data[2]), int)
            print(type(write_data[3]), str)
            print(type(write_data[4]), float)

            return False

        else:

            return True

    def write_to_table(self, write_data):

        open_connection = self.open_connection()

        cursor = open_connection.cursor()

        sqlite_insert_str = \
            """INSERT INTO runs values (?, ?, ?, ?, ?)"""

        cursor.execute(sqlite_insert_str, (write_data))

        open_connection.commit()

        open_connection.close()

