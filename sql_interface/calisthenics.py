import sqlite3
import sql_interface.interface as Table

class calisthenics(Table):
    """
    TODO(Oliver) add in specific functions here.


    """
    table_name = "calisthenics"

    def write_to_calisthenics(self):
        """
        :return: no return, just inserts into database
        """
        open_connection = self.connection()

        cursor = open_connection.cursor()

        sqlite_insert_str = \
            """INSERT INTO %s values (?, ?, ?, ?, ? ,?)""" % self.table_name

        cursor.execute(sqlite_insert_str, self.write_data)

        open_connection.commit()

        open_connection.close()