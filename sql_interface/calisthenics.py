from sql_interface.interface import Table
import datetime


class Calisthenics(Table):
    """
    TODO(Oliver) add in specific functions here.


    """

    def __init__(self, param):
        super().__init__(param)
        self.table_name = "calisthenics"

    def cali_data_check(self, write_data) -> bool:
        """

        :return: throws error if wrong data types
        """
        if \
        type(write_data[0]) != datetime.date or \
        type(write_data[1]) != int or \
        type(write_data[2]) != int or \
        type(write_data[3]) != int or \
        type(write_data[4])  != str or \
        type(write_data[5]) != float:

            print(type(write_data[0]), datetime.date)
            print(type(write_data[1]), int)
            print(type(write_data[2]), int)
            print(type(write_data[3]), int)
            print(type(write_data[4]), str)
            print(type(write_data[5]), float)


            return False

        else:

            return True

    #TODO move this to parent class, take INSERT str as variable
    def write_to_table(self, write_data):

        open_connection = self.open_connection()

        cursor = open_connection.cursor()

        sqlite_insert_str = \
            """INSERT INTO calisthenics values (?, ?, ?, ?, ?, ?)"""

        cursor.execute(sqlite_insert_str, write_data)

        open_connection.commit()

        open_connection.close()
