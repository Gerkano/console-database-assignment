import sqlite3
from sqlite3 import DatabaseError


class SqlDatabase:
    def __init__(self, db_name: str) -> None:
        self._conn = sqlite3.connect(db_name+".db")
        self._cursor = self._conn.cursor()

    def create_table(self, table_name: str, columns: str) -> None:
        try:
            with self._conn:
                self._cursor.execute(f"""CREATE TABLE IF NOT EXISTS
                {table_name} (
                {columns}
                )""")
        except DatabaseError:
            print("Unable to create table! Database error.")
        except Exception as e:
            print(f"Unable to create table!. Error msg: {e}")

    def write(self, table_name: str, entry_values: str) -> None:
        with self._conn:
            self._cursor.execute(f"INSERT INTO {table_name} VALUES ({entry_values})")

    def read(self, columns: str, table_name: str, where_clause: str, order_by:str) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT {columns} From {table_name} WHERE {where_clause} ORDER BY {order_by}")
            return self._cursor.fetchall()

    def read_all(self, columns: str, table_name: str) -> list:
        with self._conn:
            self._cursor.execute(f"SELECT {columns} From {table_name}")
            return self._cursor.fetchall()

    def update(self, table_name: str, update_clause: str, where_clause: str) -> None:
        with self._conn:
            self._cursor.execute(f"UPDATE ({table_name}) SET {update_clause} WHERE {where_clause}'")

    def delete(self, table_name: str, where_clause: str) -> None:
        with self._conn:
            self._cursor.execute(f"DELETE from {table_name} WHERE {where_clause}")

    def add_column(self, table_name: str, where_clause: str):
        with self._conn:
            self._cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {where_clause} INTEGER")

    def rename_column(self, table_name: str, where_clause: str):
        with self._conn:
            self._cursor.execute(f"ALTER TABLE {table_name} RENAME COLUMN {where_clause}") #<existing_column_name> TO <new_column_name>'

    def rename_table(self, table_name: str, where_clause: str):
        with self._conn:
            self._cursor.execute(f"ALTER TABLE {table_name} RENAME TO {where_clause}")

    def drop_column(self, table_name: str, where_clause: str):
        with self._conn:
            self._cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {where_clause}")

    