# exercise log
GUI for keeping track of exercise - links to an sqlite database file

##general notes

due to free access of jetbrains, I'm developing this in pycharm. Turns out pycharm has great tools for reading
.db files. To use these, I had to download SQLite JDBC driver, after having a look at data source properties. This
wasn't necessary to read the file... Pycharm now highlights errors INSERT commands, about what exists in the table.