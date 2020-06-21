import sqlite3
import utils.data_objects as data_objects

def write_to_calisthenics(connection : sqlite3.Connection,
                          data : data_objects.CalisthenicsData
                          ) -> None:
    """



    :param connection: the database connection object
    :return: no return, just inserts into database
    """
    cursor = connection.cursor()

    sqlite_insert_str = \
        """INSERT INTO calisthenics values (?, ?, ?, ?, ? ,?)"""

    cursor.execute(sqlite_insert_str, data.make_data_dict())

    connection.commit()