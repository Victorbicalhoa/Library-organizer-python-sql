import sqlite3
from pathlib import Path


class SQLiteConnector:
    def __init__(self, db_name="library.db"):
        self.db_path = Path(__file__).parent / db_name
        self.conn = None

    def connect(self):
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row  # Access columns by name
            print(f"Connected to database: {self.db_path}")
            return self.conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def close(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        """
        Execute a DML/DDL query.
        Returns a list of rows for SELECT queries.
        """
        if not self.conn:
            print("No active database connection.")
            return []

        cursor = self.conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database query error: {e}")
            self.conn.rollback()
            return []

    def create_tables(self, sql_file="create_tables.sql"):
        """
        Create tables by executing a SQL script.
        """
        sql_path = Path(__file__).parent / sql_file
        if not sql_path.exists():
            print(f"SQL file not found: {sql_path}")
            return

        with open(sql_path, "r") as f:
            sql_script = f.read()

        self.execute_query(sql_script)
        print("Tables created/updated successfully.")


if __name__ == "__main__":
    connector = SQLiteConnector()
    conn = connector.connect()

    if conn:
        connector.create_tables()
        # Example: Insert a test book
        connector.execute_query(
            """
            INSERT OR IGNORE INTO livros (titulo, autor, ano_publicacao)
            VALUES (?, ?, ?)
        """,
            ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979),
        )

        # Example: Select and print all books
        books = connector.execute_query("SELECT * FROM livros")
        for book in books:
            print(dict(book))

    connector.close()
