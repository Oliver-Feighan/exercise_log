import sqlite3
import os

class Table:
    def open_connection(self) -> sqlite3.Connection:
        """
        make a connection to the sqlite database (.db) file.

        if a file doesn't exist, sqlite3.connect will make the file. This
        is obviously bad, hence an os.path check is made to see if the
        file exists.

        Doctest for failed connection?
        :param db_file_name: the name of the file
        :return: the sqlite3.Connection class, that is the connection
        >>> table = Table({"file" : "log.db"})
        >>> success_connection = table.open_connection()
        >>> type(success_connection)
        <class 'sqlite3.Connection'>
        >>> fail_table = Table({"file" : "fail.db"})
        database file fail.db doesn't exist.
        """
        if not os.path.exists(self.file):
            print("database file %s doesn't exist." % self.file)
            return None

        connection = sqlite3.connect(self.file)

        return connection

    def __init__(self, params):
        self.file = params.get("file", "log.db")
        self.connection = self.open_connection()
        self.write_data = params.get("data")

    def close_connection(self):
        self.connection.close()

    def write_to_table(self):
        """
        :return: no return, just inserts into database
        """
        open_connection = self.connection()

        cursor = open_connection.cursor()

        sqlite_insert_str = \
            """INSERT INTO %s values""" % self.table_name

        cursor.execute(sqlite_insert_str, self.write_data)

        open_connection.commit()

        open_connection.close()







