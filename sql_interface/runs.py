import sqlite3
import sql_interface.interface as Table


class runs(Table):
    """
    TODO(Oliver) add in specific functions here.


    """
    table_name = "runs"

    def run_data_check(self):
        type(self.write_data(0)) ==

    def write_to_runs(self):
        """
        :return: no return, just inserts into database
        """
        cursor = self.connection.cursor()

        sqlite_insert_str = \
            """INSERT INTO %s values (?, ?, ?, ?, ?)""" % self.table_name

        cursor.execute(sqlite_insert_str, self.write_data)

        self.connection.commit()