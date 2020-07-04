import gui.master_window
import sql_interface.runs
import sql_interface.calisthenics


def main():
    run_table_interface = sql_interface.runs.Runs({"file" : "log.db"})
    calisthenics_table_interface = sql_interface.calisthenics.Calisthenics({"file" : "log.db"})

    window = gui.master_window.MasterWindow(run_table_interface, calisthenics_table_interface)

if __name__ == "__main__":
    main()