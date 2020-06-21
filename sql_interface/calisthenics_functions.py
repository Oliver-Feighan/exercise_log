import sqlite3
import utils.data_objects as data_objects

def write_to_calisthenics(connection : sqlite3.Connection,
                          data : data_objects.CalisthenicsData
                          ) -> None:
    """
    add the data from Data object to a database, given
    by the connetion argument

    :param connection: the database connection object
    :param data: the CalisthenicData object, containing information
                 to be added to the database
    :return: no return, just inserts into database
    """

    cursor = connection.cursor()

    sqlite_insert_str = \
        """INSERT INTO calisthenics values (?, ?, ?, ?, ? ,?)"""

    cursor.execute(sqlite_insert_str, data.make_data_tuple())

    connection.commit()