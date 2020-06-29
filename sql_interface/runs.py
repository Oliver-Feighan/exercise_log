from sql_interface.interface import Table
import datetime

class Runs(Table):
    """
    TODO(Oliver) add in specific functions here.


    """
    table_name = "runs"

    def run_data_check(self, write_data) -> bool:
        """

        :return: exits program if
        """
        if \
        type(write_data[0]) != type(datetime.datetime.now().date()) or \
        type(write_data[1]) != str or \
        type(write_data[2]) != int or \
        type(write_data[3]) != str or \
        type(write_data[4]) != float:

            return False

        else:

            return True