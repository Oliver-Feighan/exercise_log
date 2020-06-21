import sqlite3
import os

def open_connection(db_file_name : str) -> sqlite3.Connection:
    """
    make a connection to the sqlite database (.db) file.

    if a file doesn't exist, sqlite3.connect will make the file. This
    is obviously bad, hence an os.path check is made to see if the
    file exists.

    Doctest for failed connection?
    :param db_file_name: the name of the file
    :return: the sqlite3.Connection class, that is the connection
    >>> success_connection = open_connection('log.db')
    >>> type(success_connection)
    <class 'sqlite3.Connection'>
    >>> fail_connection = open_connection('fail.db')
    database file fail.db doesn't exist.
    """
    if not os.path.exists(db_file_name):
        print("database file %s doesn't exist." % db_file_name)
        return None

    connection = sqlite3.connect(db_file_name)

    return connection
