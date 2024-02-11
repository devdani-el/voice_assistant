import sqlite3

class nick:
    def user(self):
        info = {
            'name': 'user main'
        }

        conn = sqlite3.connect("username.db")
        cursor = conn.cursor()

        try:
            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS user
                        (
                        name_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                        username        TEXT,
                        display_order   INTEGER
                        )''')
            conn.commit()

            try:
                cursor.execute('''INSERT INTO user (username, display_order)
                                VALUES (?, (SELECT IFNULL(MAX(display_order), 0) + 1 FROM user))''', (info['name'],))
                cursor.execute('''UPDATE user SET username = ? WHERE name_id = (SELECT MAX(name_id) FROM user)''', (info['name'],))
                conn.commit()
                print(f"New name '{info['name']}' has been stored in the database.")
            except sqlite3.Error as e:
                print(f"Error inserting into the database: {e}")
                conn.rollback()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            conn.rollback()
        finally:
            conn.close()

        return info


class data_tasks:
    def create_task_table(self):
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


    def add_task_to_db(self, message):
        try:
            with sqlite3.connect("tasks.db") as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO tasks (message, display_order)
                            VALUES (?, (SELECT IFNULL(MAX(display_order), 0) + 1 FROM tasks))''', (message,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting into the database: {e}")


    def show_all_tasks():
        conn = sqlite3.connect("tasks.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
            table_exists = cursor.fetchone()
            if table_exists:
                cursor.execute("SELECT * FROM tasks ORDER BY display_order")
                all_tasks = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            conn.close()


    def delete_task_keyword(self, keyword):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM tasks WHERE message LIKE ?', ('%' +keyword+ '%',))
            conn.commit()
        except sqlite3.Error as e:
            print("Error when deleting task:", e)


    def delete_all_tasks(self):
        conn = sqlite3.connect('tasks.db')
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM tasks')
            conn.commit()
        except sqlite3.Error as e:
            print("Error when deleting task:", e)
        finally:
            conn.close()
        