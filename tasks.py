import sqlite3


def create_task_table():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    try:
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS tasks
                    (
                    task_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                    message         TEXT,
                    display_order   INTEGER
                    )''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
        conn.rollback()
    finally:
        conn.close()


def add_task_to_db(message):
    try:
        with sqlite3.connect("tasks.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO tasks (message, display_order)
                        VALUES (?, (SELECT IFNULL(MAX(display_order), 0) + 1 FROM tasks))''', (message,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting into the database: {e}")
        conn.rollback()
    finally:
    # Close the connection (if not using a context manager)
        conn.close()


def show_all_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
        table_exists = cursor.fetchone()
        if table_exists:
            tasks = cursor.execute("SELECT * FROM tasks ORDER BY display_order")
            all_tasks = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def delete_task_keyword(keyword):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    try:
        cursor.execute('SELECT task_id FROM tasks message LIKE ?', ('%' +keyword+ '%',))
        tasks_to_delete = cursor.fetchall()

        with sqlite3.connect("tasks.db") as conn:
            cursor = conn.cursor()
    except sqlite3.Error as e:
        print("Error when deleting task:", e)


def delete_all_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM tasks')
        conn.commit()
    except sqlite3.Error as e:
        print("Error when deleting task:", e)
    