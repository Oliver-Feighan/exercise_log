# exercise log
GUI for keeping track of exercise - links to an sqlite database file

##general notes

due to free access of jetbrains, I'm developing this in pycharm. Turns out pycharm has great tools for reading
.db files. To use these, I had to download SQLite JDBC driver, after having a look at data source properties. This
wasn't necessary to read the file... Pycharm now highlights errors INSERT commands, about what exists in the table.

.connection() function makes a connection to the database file, 
and this is fine for reading from database file. To write (maybe 
other stuff?) a cursor needs to be made. eg:

`connection = sqlite3.connection('db_file.db')`<br/>
`cursor  = connection.cursor()`

wild. Also need to commit these changes:

`#do some commands`<br/>
`cursor.execute(" ........ ")`<br/>
`connection.commit()`


