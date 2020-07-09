#!/usr/bin/env python

from gui.master_window import *
from sql_interface.runs import *
from sql_interface.calisthenics import *

def main():
    run_table_interface = Runs({"file" : "log.db"})
    calisthenics_table_interface = Calisthenics({"file" : "log.db"})

    window = MasterWindow(run_table_interface, calisthenics_table_interface)

if __name__ == "__main__":
    main()