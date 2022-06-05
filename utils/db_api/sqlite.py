import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)
    
    def create_table_films(self):
        sql = """
        CREATE TABLE films(
            name varchar(255) NOT NULL,
            about TEXT,
            photo varchar(255),
            link varchar(255) NOT NULL,
            PRIMARY KEY (link)
            );
"""
        self.execute(sql, commit=True)

    def create_table_channel(self):
        sql = """
        CREATE TABLE channel(
            link varchar(255) NOT NULL,
            PRIMARY KEY (link)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def add_film(self, name: str, photo, about: str, link: str):
        sql = """
        INSERT INTO films(name, photo, about, link) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(name, photo, about, link), commit=True)

    def add_channel(self, link: str|int):
        sql = """
        INSERT INTO channel(link) VALUES(?)
        """
        self.execute(sql, parameters=(link,), commit=True)

    def search_film(self, q):
        sql = """
        SELECT * FROM films WHERE name LIKE ? ORDER by name
        """
        return self.execute(sql, parameters=(q,), fetchall=True)

    def get_channel(self):
        sql = """
        SELECT * FROM channel
        """
        return self.execute(sql, fetchall=True)

    def delete_list_film(self, q):
        sql = """
        SELECT * FROM films WHERE name LIKE ?
        """
        return self.execute(sql, parameters=(q,), fetchall=True)

    def delete_film(self, link):
        sql = """
        DELETE FROM films WHERE link=?
        """
        self.execute(sql, parameters=(link,), commit=True)

    def delete_channel(self, link):
        sql = """
        DELETE FROM channel WHERE link=?
        """
        self.execute(sql, parameters=(link,), commit=True)

    def sorted_movie(self):
        sql = """
        SELECT * FROM films ORDER BY name
        """
        return self.execute(sql, fetchall=True)

    def count_movies(self):
        return self.execute("SELECT COUNT(*) FROM films;", fetchone=True)


    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM films WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________
Executing:
{statement}
_____________________________________________________
""")
