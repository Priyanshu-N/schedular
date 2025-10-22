import sqlite3
con = sqlite3.connect('timers.db')

cur = con.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS scheduling_time
            (id int, task_name text, task_type varchar, 
            process_name varchar, start_time datetime,
            end_time datetime,
            updated_at datetime)''')